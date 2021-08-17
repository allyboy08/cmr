from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        
    def test_sign_up_form(self):
        self.browser.get(self.live_server_url)
        
        form = self.browser.find_element_by_tag_name('h3').text,
        self.assertIn('LOGIN', form)
        
        username_inputbox = self.browser.find_element_by_name('username')
        self.assertEqual(
            username_inputbox.get_attribute('placeholder'),
            'Username...'
        )
    
        password_inputbox = self.browser.find_element_by_name('password')
        self.assertEqual(
            password_inputbox.get_attribute('placeholder'),
            'Password...'
        )
        
        submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        # He types account information the input boxes
        username_inputbox.send_keys('dennis1')
        password_inputbox.send_keys('bobross21')
        submit_btn.click()

        # He submits the form
        # username_inputbox.send_keys(Keys.submit)
        
        
        
        
   
    
    # def test_sign_up_link_redirects_to_sign_up_page(self):
    #     self.browser.get(self.live_server_url)
        
        
    #     register_url = self.live_server_url + reverse('register')
    #     self.browser.find_element_by_tag_name('a').click()
    #     self.assertEquals(
    #         self.browser.current_url,
    #         register_url
    #     )
        
    
        
    
    