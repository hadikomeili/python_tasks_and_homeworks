from django.db import models
from datetime import datetime

# Create your models here.

class Table(models.Model):
    table_number = models.CharField(max_length=3)
    cafe_space_position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.table_number}"


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class MenuItems(models.Model):
    name = models.CharField(max_length=30, verbose_name='menu item name', help_text='enter menu item name', null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='menu item category', help_text='define category', null=False, blank=False)
    discount = models.IntegerField(verbose_name='item discount', help_text='enter item discount', null=True, blank=True, default=0)
    price = models.FloatField(verbose_name='item price', help_text='enter item price', null=False, blank=False)
    image = models.FileField(verbose_name='item image', help_text='upload image of item', null=True, blank=False, upload_to='cafe5/menu_items/images/')
    create_timestamp = models.DateTimeField(verbose_name='date of adding item', help_text='date of creation of item', auto_now_add=True, null=False, blank=False)
    modify_timestamp = models.DateTimeField(verbose_name='date of update item', help_text='date of modify of item', auto_now=True, null=False, blank=False)

    def __str__(self):
        return f"{self.id}# {self.name} : {self.price}"


class Orders(models.Model):
    order_number = models.IntegerField()
    status = models.CharField(max_length=50)
    time_stamp = models.DateTimeField(auto_now_add=True)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_item_id = models.ForeignKey(MenuItems, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order_number}"


class Receipts(models.Model):
    total_price = models.FloatField()
    final_price = models.FloatField()
    time_stamp = models.DateTimeField(datetime.now())
    orders_id = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.final_price}"


