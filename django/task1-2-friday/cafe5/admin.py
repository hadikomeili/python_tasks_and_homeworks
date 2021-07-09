from django.contrib import admin
from .models import Table, MenuItems, Orders, Receipts
# Register your models here.


admin.site.register(Table)
admin.site.register(MenuItems)
admin.site.register(Orders)
admin.site.register(Receipts)
