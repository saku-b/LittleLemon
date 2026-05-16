from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        Menu.objects.create(title="Pizza", price=12.00, inventory=30)
        Menu.objects.create(title="Burger", price=8.50, inventory=20)

    def test_getall(self):

        response = self.client.get('/restaurant/menu/')

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)