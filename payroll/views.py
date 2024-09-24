from django.http import HttpResponse
from django.shortcuts import render
from operations import Payroll

def Basic_Payroll(request):
	if request.is_ajax():
		return HttpResponse(Payroll(request).Basic_Payroll())

def Delete_Payroll(request):
	if request.is_ajax():
		return HttpResponse(Payroll(request).Delete_Payroll())