from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponse
# Create your views here.



def orders_list(request):
    orders = Orders.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})


def order_details(request, order_num):
    try:
        order = Orders.objects.get(order_number=order_num)
        return render(request, 'order_detail.html', {'detail': order})
    except Orders.DoesNotExist:
        raise Http404('invalid order number')

def add_order(request):
    if request.method == 'POST':
        try:
            order = Orders.objects.create(
                order_number=request.POST['order_number'],
                status=request.POST['status'],
                time_stamp=request.POST['timestamp'],
                table_id=request.POST['table_number'],
                menu_item_id=request.POST['menu_item_id']
            )
            print(order)
            return HttpResponse("new order added!!!")
        except:
            return HttpResponse("invalid order")
    else:
        return render(request, 'add_order.html')




