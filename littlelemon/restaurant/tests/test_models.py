from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Pancakes", price=50, inventory=15)
        self.assertEqual(item.__str__(), 'Pancakes : 50')