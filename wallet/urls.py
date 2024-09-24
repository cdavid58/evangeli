from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Get_Pass_Invoice/$',Get_Pass_Invoice,name="Get_Pass_Invoice"),
	url(r'^Create_Pass_Invoice/$',Create_Pass_Invoice,name="Create_Pass_Invoice"),
]