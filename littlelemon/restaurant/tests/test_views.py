from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(cls):
        cls.item1 = item = Menu.objects.create(title="Steak", price=150, inventory=5)
        cls.item2 = item = Menu.objects.create(title="Soup", price=20, inventory=65)

    def test_getall(self):
        serializer_it1 = MenuSerializer(self.item1)
        serializer_it2 = MenuSerializer(self.item2)
        assert serializer_it1.data == {'id': 2, 'title': 'Steak', 'price': '150.00', 'inventory': 5}
        assert serializer_it2.data == {'id': 3, 'title': 'Soup', 'price': '20.00', 'inventory': 65}