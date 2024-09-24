from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Report_Invoices/(\d+)/$',Report_Invoices,name="Report_Invoices"),
	url(r'^Report_Invoice_Annulled/(\d+)/$',Report_Invoice_Annulled,name="Report_Invoice_Annulled"),
	url(r'^List_Best_Selling_Product/$',List_Best_Selling_Product,name="List_Best_Selling_Product"),
	url(r'^Close_The_Box/$',Close_The_Box,name="Close_The_Box"),
	url(r'^Inventory_History/$',Inventory_History,name="Inventory_History"),
	url(r'^Get_All_History_Pass_Invoice/$',Get_All_History_Pass_Invoice,name="Get_All_History_Pass_Invoice"),
]