from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Index/$',Index,name="Index"),
	url(r'^Settings/$',Settings,name="Settings"),
	url(r'^Get_Selling_By_Date/$',Get_Selling_By_Date,name="Get_Selling_By_Date"),
]