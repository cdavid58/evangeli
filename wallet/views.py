from django.http import HttpResponse
from django.shortcuts import render
from operations import Wallet, Invoice

def Get_Pass_Invoice(request):
	data = Wallet(request).Get_Pass_Invoice()
	print(data)
	return render(request,'wallet/cxc.html',{'page_obj': data})

def Create_Pass_Invoice(request):
	if request.is_ajax():
		return HttpResponse(Invoice(request).Create_Pass_Invoice())