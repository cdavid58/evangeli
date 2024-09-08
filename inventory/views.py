from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from operations import Inventory, Supplier, Setting
import json

def Get_List_Products(request):
	data = Inventory(request).Get_List_Products()
	items_per_page = 10
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'inventory/list_inventory.html', {'page_obj': data})

def Create_Category_(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Create_Category())

def Create_Subcategory_(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Create_Subcategory())

def Create_Product(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Create_Product())
	return render(request,'inventory/add.html',{'cat': Inventory(request).Get_Category(), 'supplier':Supplier(request).List_Supplier(), 'unit_measures': Setting(request).Get_All_Unit_Measures()})

def Get_Subcategory(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Get_List_SubCategory())

def Load_Inventory_Excel(request):
	if request.is_ajax():
		import json
		result = None
		excel = 1
		for i in json.loads(request.POST['data']):
			for j in i:
				_data = j
				request.GET = j
				result = Inventory(request).Create_Product(excel = excel)
				excel = 0
		return HttpResponse(result)

def Delete_Product(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Delete_Product())


def Edit_Product(request, code):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Update_Product(request))
	return render(request,'inventory/edit.html',{'p':Inventory(request).Get_Product(code), 
					'cat': Inventory(request).Get_Category(),
					'supplier':Supplier(request).List_Supplier()
				})

def Transfer(request):
	Inventory(request).Return_Products()
	return render(request,'inventory/transfer.html',{
		'list_branch': Inventory(request).List_Branch(),
		'product':Inventory(request).Get_List_Products()
		})


def Save_Transfer(request):
	if request.is_ajax():
		_data = request.POST
		data = json.loads(_data['headers'])
		data['pk_employee'] = request.session['pk_employee']
		data['branch_sends'] = request.session['pk_branch']
		data['details'] = json.loads(_data['items'])
		return HttpResponse(Inventory(request).Save_Transfer(data))