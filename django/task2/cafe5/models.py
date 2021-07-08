from django.db import models
from datetime import datetime

# Create your models here.

class Table(models.Model):
    table_number = models.IntegerField()
    cafe_space_position = models.CharField(max_length=100)

    def __str__(self):
        return f"table: {self.table_number}"

class MenuItems(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    discount = models.IntegerField()
    price = models.FloatField()
    serving_time_period = models.IntegerField()
    estimated_cooking_time = models.IntegerField()

    def __str__(self):
        return f"item name: {self.name}"

class Orders(models.Model):
    order_number = models.IntegerField()
    status = models.CharField(max_length=50)
    time_stamp = models.DateTimeField(datetime.now())
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_item_id = models.ForeignKey(MenuItems, on_delete=models.CASCADE)

    def __str__(self):
        return f"order number: {self.order_number} , status: {self.status}"


class Receipts(models.Model):
    total_price = models.FloatField()
    final_price = models.FloatField()
    time_stamp = models.DateTimeField(datetime.now())
    orders_id = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def __str__(self):
        return f"final price: {self.final_price}"


