from django.http import HttpResponse
from from_number_to_letters import Thousands_Separator
from django.core.paginator import Paginator
from django.shortcuts import render
from operations import Report, Wallet
import report_pdf, env

def Report_Invoices(request, type_document):
	invoice = "Facturas Electrónicas" if type_document == '2' else "Facturas POS"
	data = Report(request).Report_Invoices(type_document)
	total = 0
	for i in data:
		total += int(i['total'])
	return render(request,'report/report_invoices.html', {'page_obj': data,'invoice':invoice,'total':Thousands_Separator(total)})

def List_Best_Selling_Product(request):
	data = Report(request).Get_All_List_Best_Selling_Product()
	items_per_page = 20
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'report/report_get_list_best_selling_product.html', {'page_obj': page_obj})


def Report_Invoice_Annulled(request, type_document):
	invoice = "Facturas Electrónicas Anuladas" if type_document == '2' else "Facturas POS Anuladas"
	data = Report(request).Report_Invoice_Annulled(type_document)
	total = 0
	for i in data:
		total += int(i['total'])
	return render(request,'report/report_invoices.html', {'page_obj': data,'invoice':invoice})

def Close_The_Box(request):
	if request.is_ajax():
		data_invoice = Report(request).Close_The_Box_All()
		result = report_pdf.PDF(request.GET['date_start'], request.GET['date_end'],data_invoice[0], f"{env.URL_FILES}{request.session['pk_branch']}", request.session['name_branch'])
		return HttpResponse(result)

def Inventory_History(request):
	if request.is_ajax():
		return HttpResponse(Report(request).History_Inventory())


def Get_All_History_Pass_Invoice(request):
	return render(request,'report/history_pass_invoice.html',{'page_obj':Wallet(request).Get_All_History_Pass_Invoice()})