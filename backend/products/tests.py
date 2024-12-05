from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product

# Create your tests here.

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            'name': 'Test Product',
            'description': 'A test product',
            'price': 19.99,
            'stock': 10
        }
        self.product = Product.objects.create(**self.product_data)

    def test_create_product(self):
        # Test creating a new product
        new_product_data = {
            'name': 'Another Test Product',
            'price': 29.99,
            'stock': 5
        }
        response = self.client.post('/api/products/', new_product_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 2)

    def test_get_products(self):
        # Test retrieving products
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)