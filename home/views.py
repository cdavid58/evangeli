from from_number_to_letters import Thousands_Separator
from datetime import datetime, timedelta, date
from django.http import HttpResponse
from operations import Setting, Report, Invoice
from django.shortcuts import render
import env

def Index(request):
	date_now = datetime.now()
	new_date = date_now + timedelta(days=7)
	_data = {
		"pk_branch":request.session['pk_branch'],
	    "start_date":date.today(),
	    "end_date":new_date.strftime("%Y-%m-%d")
	}
	invoice = Invoice(request)
	pos = invoice.Get_Selling_By_Invoice(15)['total']
	elec = invoice.Get_Selling_By_Invoice(1)['total']
	nc = invoice.Get_Selling_By_Invoice(4)['total']
	nd = invoice.Get_Selling_By_Invoice(4)['total']
	ds = invoice.Get_Selling_By_Invoice(5)['total']
	total_selling = (pos + elec + nd) - (nc + ds)
	data = Report(request).Get_List_Best_Selling_Product(_data)
	return render(request,'index.html',{
				'data':data,
				'pos':Thousands_Separator(pos),
				'elec':Thousands_Separator(elec),
				'nc':Thousands_Separator(nc),
				'nd':Thousands_Separator(nd),
				'ds':Thousands_Separator(ds),
				'total_selling':Thousands_Separator(total_selling),
				'total_selling_gra':total_selling
				})

def Get_Selling_By_Date(request):
	if request.is_ajax():
		return HttpResponse(Invoice(request).Get_Selling_By_Date(request.GET))


def Settings(request):
	data_company = Setting(request).Get_Branch()
	return render(request,'settings/company.html',{'branch':data_company, 'r':Setting(request).Get_Resolution_List()})