from operations import Invoice, Customer, Inventory, Setting
from from_number_to_letters import Thousands_Separator
from django.core.paginator import Paginator
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from jinja2 import Environment, FileSystemLoader
import os, json, requests, env, make_pdf


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
		'totals': Thousands_Separator(subtotals + ipo + tax)
	}
	page_invoice = 'Pos Electrónico'
	if int(data['type_document']) == 2:
		page_invoice = 'elect'
	print(int(data['type_document']))
	return render(request,f'invoice/pos.html',{
		'invoice':data,
		'details':data['details'],
		'paymentmethodinvoice':data['payment_form'],
		'totals':totals,
		'client':data['customer'],
		'company':data['branch'],
		'number':data['resolution']['_from'],
		'type_document':int(data['type_document']),
	})

def Annulled_Invoice_By_Product(request):
	if request.is_ajax():
		invoice = Invoice(request).Annulled_Invoice_By_Product()
		return HttpResponse(invoice)