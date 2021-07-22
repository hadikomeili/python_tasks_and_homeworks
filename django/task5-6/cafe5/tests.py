from django.test import TestCase
from datetime import datetime
from .models import *

# Create your tests here.


class MenuItemsTest(TestCase):

    def setUp(self) -> None:
        cat1 = Category.objects.create(name='irani')
        cat2 = Category.objects.create(name='fast food')
        menu_item1 = MenuItems.objects.create(name='mi1', category=cat1, discount=10, price=10000)
        menu_item2 = MenuItems.objects.create(name='mi2', category=cat2, discount=110, price=20000)
        menu_item3 = MenuItems.objects.create(name='mi3', category=cat1, discount=-5, price=30000)
        menu_item4 = MenuItems.objects.create(name='mi4', category=cat2, discount=5, price=-25000)
        menu_item5 = MenuItems.objects.create(name='mi1', category=cat1, discount=10, price=12000.50)
        menu_item6 = MenuItems.objects.create(name='mi1', category=cat1, discount=8, price='12000')
        menu_item7 = MenuItems.objects.create(name='mi1', category=cat1, price=8000)
        self.mi1 = MenuItems.final_price(menu_item1)
        self.mi2 = MenuItems.final_price(menu_item2)
        self.mi3 = MenuItems.final_price(menu_item3)
        self.mi4 = MenuItems.final_price(menu_item4)
        self.mi5 = MenuItems.final_price(menu_item5)
        self.mi6 = MenuItems.final_price(menu_item6)
        self.mi7 = MenuItems.final_price(menu_item7)
        # print(self.mi1)

    def test_menu_item_final_price_mi1(self):
        self.assertEqual(self.mi1, 9000)

    def test_menu_item_final_price_mi5(self):
        self.assertEqual(self.mi5, 10800.45)

    def test_menu_item_final_price_mi1_by_empty_discount(self):
        self.assertEqual(self.mi7, 8000)

    def test_menu_item_final_price_mi2_discount_greater_than_100(self):
        self.assertRaises(AssertionError, MenuItems.final_price, 'menu_item2')

    def test_menu_item_final_price_mi3_negative_discount(self):
        self.assertRaises(AssertionError, MenuItems.final_price, 'menu_item3')

    def test_menu_item_final_price_mi4_negative_price(self):
        self.assertRaises(AssertionError, MenuItems.final_price, 'menu_item4')

    def test_menu_item_final_price_mi5_string_price(self):
        self.assertRaises(AssertionError, MenuItems.final_price, 'menu_item4')


class TimestampMixinTest(TestCase):

    def setUp(self) -> None:
        self.u1 = Cashier.objects.create(username='hadi', password='123', email='asd@a.com')

    def test_timstampmixin_delete_timestamp(self):
        self.assertEqual(self.u1.delete_timestamp, None)

    def test_timstampmixin_delete_timestamp2(self):
        self.u1.delete_timestamp = datetime.now()
        self.u1.save()
        self.assertNotEqual(self.u1.delete_timestamp, None)

    def test_timstampmixin_delete_timestamp_greater_than_now(self):
        self.u1.delete_timestamp = datetime.now() + timedelta(days=5)
        self.u1.save()
        self.assertGreater(self.u1.delete_timestamp, datetime.now())





