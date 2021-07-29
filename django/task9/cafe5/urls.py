from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'cafe5'

urlpatterns = [
    path('orders/', orders_list, name='all_orders'),
    path('add_order/', add_order, name='add_order'),
    path('order/<int:order_num>', order_details, name='order_details'),
    path('add_new_order', AddOrderView.as_view(), name='add_new_order_by_class_view'),
    path('orders_list/', OrderList.as_view(), name='orders_list_by_class_view'),
    path('o/<int:number>', OrderDetails.as_view(), name='order_details_by_class_view'),
    path('allorders/', AllOrders.as_view(), name='all_orders_generic_view'),
    path('<int:pk>', OrderDetails2.as_view(), name='order_details_generic_view'),
    path('addneworder/', AddNewOrder.as_view(), name='add_new_order_generic_view'),
    path('menu_item/', menu_item_view_form, name='menu_item_by_dj_form'),
    path('create_menu_item', CreateMenuItemFormView.as_view(), name='menu_item_by_dj_model_form_view'),
    path('login/', LoginView.as_view(), name='login_cashier'),
    path('profile/', CashierProfile.as_view(), name='cashier_profile'),

]