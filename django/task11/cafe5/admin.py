from django.contrib import admin
from .models import Table, MenuItems, Orders, Receipts, Category, Cashier
from datetime import datetime

# Register your models here.


admin.site.register(Table)

admin.site.register(Orders)
admin.site.register(Receipts)
admin.site.register(Category)
admin.site.register(Cashier)


class MenuItemAdmin(admin.ModelAdmin):
    readonly_fields = ('create_timestamp', 'modify_timestamp',)
    list_filter = ['category', 'price', 'discount']
    list_display = ['name', 'category', 'price', 'deleted']
    list_editable = ['price']
    search_fields = ['name']


admin.site.register(MenuItems, MenuItemAdmin)


def logical_delete(modeladmin, request, queryset):
    queryset.update(deleted=True)


admin.site.add_action(logical_delete)
