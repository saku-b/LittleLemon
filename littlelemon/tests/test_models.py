from django.test import TestCase
from restaurant.models import Menu # Fixed absolute import

class MenuTest(TestCase):
    def test_get_item(self):
        # Create a temporary test record
        item = Menu.objects.create(title="IceCream", price=80.00, inventory=100)
        # Assert that the string output matches our format expectation
        self.assertEqual(str(item), "IceCream : 80.00")