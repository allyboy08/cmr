from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Customer
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.customer1 = Customer.objects.create(
            user='bob',
            name='kevin',
            phone='0123456789',
            email='test@gmail.com'
        )
        
    
    def test_home_GET(self):
        
        response = self.client.get(self.home_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')