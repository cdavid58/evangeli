from operations import Invoice, Customer, Inventory, Setting
from from_number_to_letters import Thousands_Separator
from django.core.paginator import Paginator
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from jinja2 import Environment, FileSystemLoader
import os, json, requests, env, make_pdf, base64, io, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def cargar_tabs(request):
    return render(request, 'invoice/tabs.html')

def Validated_Quantity(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Validated_Quantity())

def Type_Document(n):
	value = None 
	if int(n) ==  1:
		value = "Facturas Electrónicas"
	elif int(n) ==  4:
		value = "Nota Crédito"
	return value
	
def Get_List_Invoice(request,type_document):
	data = Invoice(request).Get_List_Invoice(type_document)
	items_per_page = 20
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	request.session['type_document'] = type_document
	request.session['invoice_identifier'] = Type_Document(type_document)
	return render(request,'invoice/list_invoice.html', {'page_obj': page_obj, 'type_invoice': type_document} )

def Send_Invoice_DIAN(request):
	if request.is_ajax():
		return HttpResponse(Invoice(request).Send_Invoice_DIAN())

def Annulled_Invoice(request):
	if request.is_ajax():
		return HttpResponse(Invoice(request).Annulled_Invoice())

def View_Invoice(request, pk):
	data = Invoice(request).Get_Invoice(pk)
	subtotal = 0
	tax = 0
	ipo = 0
	discount = 0
	for i in data['details']:
		subtotal += float(i['price']) * float(i['quantity'])
		tax += float(i['tax']) * float(i['quantity'])
		ipo += float(i['ipo']) * float(i['quantity'])
		discount += float(i['discount']) * float(i['quantity'])
	total = subtotal + tax + ipo
	consumption_tax = 0
	if data['consumption_tax']:
		consumption_tax = (total * (int(data['branch']['consumption_tax']) / 100))
	total += consumption_tax
	return render(request,'invoice/invoice.html',{'data':data, 'sub':subtotal, 'tax': tax, 'totals': total, 'ipo':ipo, 'discount': discount,'consumption_tax':consumption_tax})

def GetPDF(request,pk):
	data = Invoice(request).Get_Invoice(pk)
	data['logo'] = request.session['logo']	
	path_dir = f"{env.URL_FILES}{request.session['pk_branch']}"
	if not os.path.exists(path_dir):
		os.mkdir(path_dir)
	data['path_dir'] = path_dir
	make_pdf.Create_PDF_Invoice(data)
	path_dir = f"{path_dir}/FES-{data['prefix']}{data['number']}.pdf"
	
	return FileResponse(open(path_dir,'rb'),content_type='application/pdf')

def Get_Number(request):
	if request.is_ajax():
		return HttpResponse(Setting(request).Get_Resolution({"type_document": request.GET['type_document'], "pk_branch": request.session['pk_branch']}))

def Return_Products(request):
	if request.is_ajax():
		Inventory(request).Return_Products()
		return HttpResponse(True)

def Return_Product_UNIQUE(request):
	if request.is_ajax():
		Inventory(request).Return_Product_UNIQUE()
		return HttpResponse(True)

def Create_Invoice(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Product_Reserved())
	Inventory(request).Return_Products()
	return render(request,'invoice/order.html',{
		'client':Customer(request).Get_List_Customer(),
		'product':Inventory(request).Get_List_Products()
	})

def Loading_Product(request):
	if request.is_ajax():
		return HttpResponse(json.dumps(Inventory(request).Get_Product(request.GET['code'])))
	
def Save_Invoice(request):
	if request.is_ajax():
		headers_json = json.loads(request.POST.get('headers'))
		details_invoice_json = json.loads(request.POST.get('details_invoice'))
		paymentform = paymentform = {
		    "paymentform": 1,
		    "paymentmethod": 10,
		    "due_date": headers_json['date']
		}
		if int(headers_json['paymentform']) == 2:
			paymentform = {
		        "paymentform": 2,
		        "paymentmethod": 30,
		        "due_date": headers_json['date_invoice_due']
		    }
		data = headers_json
		data['details'] = details_invoice_json
		data['payment_form'] = paymentform
		result = Invoice(request).Create_Invoice(data)
		return HttpResponse(result)


def Print_Invoice(request,pk):
	payload = json.dumps({"pk_invoice": pk})
	headers= {'Content-Type':'application/json'}
	response = requests.request("GET", env.GET_INVOICE, headers=headers, data=payload)
	data = json.loads(response.text)
	data['time'] = str(data['time'])[:5]
	subtotals = 0
	tax = 0
	ipo = 0
	discount = 0
	for i in data['details']:
		quantity = float(i['quantity'])
		subtotals += round(float(i['subtotals']))
		tax += float(i['tax']) * quantity
		ipo += float(i['ipo']) * quantity
		discount += float(i['discount']) * quantity
	totals = {
		"subtotals":Thousands_Separator(subtotals),
		"tax":Thousands_Separator(tax),
		"ipo":Thousands_Separator(ipo),
		"discount":Thousands_Separator(discount),
		'totals': Thousands_Separator(subtotals + ipo + tax),
		'totals_with_discount': Thousands_Separator((subtotals + ipo + tax) - discount)
	}
	page_invoice = 'Pos Electrónico'
	if int(data['type_document']) == 2:
		page_invoice = 'elect'
	print(data)
	make_pdf.GenerateQR(data['QRStr'], data['number'],data['resolution']['branch'])
	qr = f'{env.URL_APPLICATION}/static/company/{data['customer']['branch']}/{str(data['number'])}.png'
	return render(request,f'invoice/ticket.html',{
		'invoice':data,
		'details':data['details'],
		'paymentmethodinvoice':data['payment_form'],
		'totals':totals,
		'client':data['customer'],
		'company':data['branch'],
		'number':data['resolution']['_from'],
		'type_document':int(data['type_document']),
		'qr': qr
	})

def Annulled_Invoice_By_Product(request):
	if request.is_ajax():
		invoice = Invoice(request).Annulled_Invoice_By_Product()
		return HttpResponse(invoice)

def base64_to_pdf(base64_string, xml,pdf,atd,request):
	result = False
	try:
		_path = f'{env.URL_FILES_SERVER}{request.session['pk_branch']}/{pdf}'
		pdf_bytes = base64.b64decode(base64_string)
		with open(_path, "wb") as pdf_file:
			pdf_file.write(pdf_bytes)

		_path = f'{env.URL_FILES_SERVER}{request.session['pk_branch']}/{atd}'
		pdf_bytes = base64.b64decode(xml)
		with open(_path, "wb") as pdf_file:
			pdf_file.write(pdf_bytes)
		result = True
	except Exception as e:
		print(e)
	return result


def enviar_email(data):
    # Configuración del servidor y las credenciales
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_usuario = f"{data['branch']['email']}"  # Cambia a tu correo
    email_contraseña = f"{data['branch']['psswd']}"  # La contraseña de aplicación de Gmail

    # Dirección de origen y de destino
    email_origen = f"{data['branch']['email']}"
    email_destino = f"{data['customer']['email']}" if int(data['customer']['identification_number']) != 222222222222 else f"{data['branch']['email']}"

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = email_origen
    mensaje['To'] = email_destino
    mensaje['Subject'] = "Asunto del correo"

    # Cuerpo del correo
    cuerpo = "Este es el cuerpo del correo electrónico enviado desde Python."
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Si quieres adjuntar un archivo (opcional)
    # archivo_adjunto = "ruta/al/archivo.txt"  # Especifica la ruta del archivo
    # adjunto = open(archivo_adjunto, "rb")

    # mime_base = MIMEBase('application', 'octet-stream')
    # mime_base.set_payload((adjunto).read())
    # encoders.encode_base64(mime_base)
    # mime_base.add_header('Content-Disposition', f"attachment; filename= {archivo_adjunto}")
    # mensaje.attach(mime_base)

    try:
        # Conectar al servidor SMTP
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()  # Iniciar la conexión TLS (encriptada)

        # Iniciar sesión en el servidor SMTP
        servidor.login(email_usuario, email_contraseña)

        # Convertir el mensaje a string y enviarlo
        texto = mensaje.as_string()
        servidor.sendmail(email_origen, email_destino, texto)

        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        servidor.quit()


def Send_Email_DIAN(request):
	if request.is_ajax():
		invoice = Invoice(request).Get_Invoice(request.GET['pk_invoice'])
		values = {
			"nit":invoice['company']['documentI'],
			"number":invoice['number'],
			"prefix": invoice['prefix'],
			"attach_document": invoice['attacheddocument'],
			"pdf": invoice['urlinvoicepdf'],
			"token": invoice['company']['token']
		}
		data = Invoice(request).pdf_to_base64(values)
		base64_to_pdf(data['pdf'],data['attach_document'],invoice['urlinvoicepdf'],invoice['attacheddocument'],request)
		enviar_email(invoice)
		return HttpResponse("")