from django.test import TestCase
from core.models import *

# Create your tests here.


class MyTestModelTest(TestCase):

    def test1_deleted(self):
        m1 = TestModel.objects.create()
        m1.deleted = True
        m1.save()

        self.assertRaises(Exception, TestModel.objects.get, id=1)

    def test2_deleted(self):
        m1 = TestModel.objects.create()
        m1.deleted = True
        m1.save()

        self.assertNotIn(m1, TestModel.objects.all())