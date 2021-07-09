from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'cafe5'

urlpatterns = [
    path('orders/', orders_list, name='all_orders'),
    path('add_order/', add_order, name='add_order'),
    path('<int:order_num>', order_details, name='order_details')

]