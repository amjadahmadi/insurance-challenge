from django.urls import path, include
from rest_framework import routers
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'engine'
urlpatterns = [

                  path('calculate/', UserInsuranceView.as_view(), name='calculate'),
              ]
