# import sys
# sys.path.append("tests/acceptance/locators")

from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Customer
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.customer1 = Customer.objects.create(
            user='bob',
            name='kevin',
            phone='0123456789',
            email='test@gmail.com'
        )
        
    
    def test_view_register_page(self):
        
        response = self.client.get(self.register_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')