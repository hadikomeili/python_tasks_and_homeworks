from django import forms
from django.core.exceptions import ValidationError
from .models import Category, MenuItems


def menu_item_name_validator(name: str):
    if not name.istitle():
        raise ValidationError('menu item name must be title!')


def menu_item_discount_validator(num: int):
    if num < 0:
        raise ValidationError('discount must be 0 or greater!')


def menu_item_price_validator(value: int):
    if value <= 0:
        raise ValidationError('price must be positive!')


class MenuItemForm(forms.Form):
    menu_item_name = forms.CharField(max_length=50, validators=[menu_item_name_validator], label='Item Name')
    discount = forms.IntegerField(validators=[menu_item_discount_validator], label='Item Discount')
    price = forms.FloatField(validators=[menu_item_price_validator], label='Item Price')
    image = forms.FileField(required=False, label='Item Image')
    category = forms.ModelChoiceField(queryset=Category.objects.all())


class MenuItemModelForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        exclude = ['create_timestamp', ['modify_timestamp']]



