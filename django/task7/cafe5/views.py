from django.core.files.storage import default_storage
from django.shortcuts import render, get_list_or_404, reverse
from django.views import View, generic

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
        print(request.POST)
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

#-------------class view

class AddOrderView(View):

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        # try:
        order = Orders.objects.create(
            order_number = self.request.POST['order_number'],
            status = self.request.POST['status'],
            time_stamp = self.request.POST['timestamp'],
            menu_item_id=self.request.POST['menu_item_id'],
            table_id = int(int(self.request.POST['table_number']))
        )

        return HttpResponse("new order added!!!")
        # except:
        #     return HttpResponse("invalid order")

    def get(self, request, *args, **kwargs):
        return render(request, 'add_order.html')


class OrderList(View):

    def get(self, request, *args, **kwargs):
        orders = Orders.objects.all()
        return render(request, 'orders_list.html', {'orders_list': orders})


class OrderDetails(View):

    def get(self, request, *args, **kwargs):

        order_number = kwargs['number']
        order = Orders.objects.get(order_number=order_number)
        return render(request, 'details.html', {'order_detail': order})


#-------------------------------------------- generic view


class AllOrders(generic.ListView):

    template_name = 'orders_list.html'
    model = Orders

class OrderDetails2(generic.DetailView):

    template_name = 'order_detail.html'
    model = Orders
    context_object_name = 'o_detail'



class AddNewOrder(generic.CreateView):

    template_name = 'add_order_generic.html'
    model = Orders
    fields = ['order_number', 'status', 'table_id', 'menu_item_id']


    def get_success_url(self):
        return reverse('cafe5:all_orders_generic_view')

#-------------------------------------------------------

from .forms import MenuItemForm


def menu_item_view_form(request):
    if request.method == 'GET':
        form = MenuItemForm()
        return render(request, 'menu_item_form.html', {'form': form})

    elif request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            default_storage.save(image.name, image)
            name = form.cleaned_data['menu_item_name']
            discount = form.cleaned_data['discount']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']
            MenuItems.objects.create(name=name, price=price, category=category, discount=discount, image=image)

            return HttpResponse('menu item created!!!')
        else:
            return render(request, 'menu_item_form.html', {'form': form})
