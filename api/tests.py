from products.models import Product
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.


BASE_URL = 'http://localhost:8000/api/products/'


class ProductApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_product_success(self):
        payload = {
            "name": "Test product",
            "code": 589,
            'price': 1200,
            'quantity': 5,
            'is_availible': True,
            'category': "computers",
        }

        res = self.client.post(BASE_URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        product = Product.objects.get(id=res.data['id'])

        print(res.data)
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(product, key))

    def test_create_product_failure(self):
        payload = {
            "code": 589,
            'price': 1200,
            'quantity': 5,
            'is_availible': True,
            'category': "computers",
        }

        res = self.client.post(BASE_URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
