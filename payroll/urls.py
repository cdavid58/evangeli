from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Basic_Payroll/$',Basic_Payroll,name="Basic_Payroll"),
	url(r'^Delete_Payroll/$',Delete_Payroll,name="Delete_Payroll"),
]