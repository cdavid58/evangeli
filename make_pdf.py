from jinja2 import Environment, FileSystemLoader
from from_number_to_letters import Thousands_Separator, numero_a_letras
import pdfkit, os, env as _env, qrcode
from getpass import getuser
USER_WINDOWS = getuser()

def GenerateQR(qr_data, number, pk):
    data = (qr_data)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    url_dir = f"{_env.URL_FILES_SERVER}{pk}/{number}.png"
    img.save(url_dir)


def GeneratePDF(name_doc, path):
    path_dir = path
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    html_file_path = os.path.join(path_dir, f"{name_doc}.html")
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdf_file_path = os.path.join(path_dir, f"{name_doc}.pdf")
    pdfkit.from_file(html_file_path, pdf_file_path, configuration=config)

def Create_PDF_Invoice(data):
    path = data['path_dir']
    env = Environment(loader=FileSystemLoader(_env.URL_FILES_TEMPLATE))
    template = env.get_template("pdf.html")
    name_doc = f"FES-{data['prefix']}{data['number']}"
    subtotal = 0
    total = 0
    ipo = 0
    tax = {}
    tax_0 = 0
    tax_5 = 0
    tax_19 = 0
    discount = 0
    GenerateQR(data['QRStr'], data['number'],data['resolution']['branch'])
    for i in data['details']:
        tax_product = int(i['tax_value'])
        if tax_product == 0:
            tax_0 += round(float(i['tax']) * float(i['quantity']))
        if tax_product == 5:
            tax_5 += round(float(i['tax']) * float(i['quantity']))
        if tax_product == 19:
            tax_19 += round(float(i['tax']) * float(i['quantity']))
        subtotal += i['subtotals']
        discount += i['discount']
        ipo += i['ipo'] * i['quantity']
        total += i['subtotals'] + (i['tax'] * i['quantity']) + (i['ipo'] * i['quantity'])
        i['total_tax'] = i['tax'] * i['quantity']
        i['quantity'] = Thousands_Separator(round(float(i['quantity'])))
        i['price'] = Thousands_Separator(round(float(i['price'])))
        i['tax'] = Thousands_Separator(round(float(i['tax'])))
        i['ipo'] = Thousands_Separator(round(float(i['ipo'])))
        i['total_tax'] = Thousands_Separator(round(float(i['total_tax'])))
        i['subtotals'] = Thousands_Separator(round(float(i['subtotals'])))
    if tax_19 > 0:
        data['tax_19'] = Thousands_Separator(tax_19)
    if tax_5 > 5:
        data['tax_5'] = Thousands_Separator(tax_5)
    if tax_0 > 0:
        data['tax_0'] = Thousands_Separator(tax_0)

    data['subtotals'] = Thousands_Separator(round(float(subtotal)))
    data['discount'] = Thousands_Separator(round(float(discount)))
    data['totals'] = Thousands_Separator(round(float(total)))
    data['ipo'] = Thousands_Separator(round(float(ipo)))
    data['total_letters'] = numero_a_letras(total).upper()
    data['type_invoice'] = int(data['type_document'])
    data['logo_qr'] = f'{_env.URL_APPLICATION}/static/company/65/{str(data['number'])}.png'
    print(data)
    html = template.render(data)
    html_file_path = os.path.join(path, f"{name_doc}.html")
    with open(html_file_path, 'w') as file:
        file.write(html)
    GeneratePDF(name_doc, path)
    os.remove(html_file_path)
