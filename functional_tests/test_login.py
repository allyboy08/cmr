from selenium import webdriver
from accounts.models import Customer
from accounts.forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestLogin(StaticLiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/allyboy08/Downloads/chromedriver_win32/chromedriver')
        
    def tearDown(self):
        self.browser.close()
        
    def test_login_form_is_displayed(self):
        self.browser.get(self.live_server_url)
        # time.sleep(50)
        
        
        form = self.browser.find_element_by_class_name('justify-content-center')
        self.assertEquals(
            form.find_element_by_tag_name('h3').text,
            'LOGIN'
        )
        
    # def test_sign_up_link_redirects_to_sign_up_page(self):
    #     self.browser.get(self.live_server_url)
        
        
    #     register_url = self.live_server_url + reverse('register')
    #     self.browser.find_element_by_tag_name('a').click()
    #     self.assertEquals(
    #         self.browser.current_url,
    #         register_url
    #     )
        
    def test_user_signs_up(self):
        self.send_keys('form-control input', 'dennis1')
        self.send_keys('form-control input', 'bobross21')
        self.browser.get(self.live_server_url)
        
        # login_url = self.live_server_url + reverse('home')
        # self.browser.find_element_by_tag_name('input').click()
        # login_url = self.live_server_url + reverse('home')
        
        self.browser.find_element_by_class_name('login_btn').click()
        # form = self.browser.find_element_by_class_name('col-md-5')
        self.assertEquals(
            form.find_element_by_tag_name('h5').text,
            'CUSTOMERS:'
        )
        
    
    