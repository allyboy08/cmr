from django.test.testcases import TransactionTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts.models import Customer
from accounts.forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth.models import User
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class TestSettings(TransactionTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/Users/allyboy08/Downloads/chromedriver_win32/chromedriver")
        # self.browser.get("https://django-livecrm1.herokuapp.com/")
        self.browser.get("http://127.0.0.1:8000/login/?next=/")
        
        
    def test_settings_form(self):
        
        form = self.browser.find_element_by_tag_name('h3').text,
        self.assertIn('LOGIN', form)
        
        # username_input = self.browser.find_element_by_name('username')
        # password_input = self.browser.find_element_by_name('password')
        
        
        # submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        
        # username_input.send_keys('okay9')
        # password_input.send_keys('working8')
        

        # submit_btn.click()
        
        # self.browser.find_element_by_class_name("nav-link").click()
        
       
       
       
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.NAME, "username")))
            self.username.send_keys("okay9")
            self.password1 = self.browser.find_element_by_name("password")
            self.password1.send_keys("working8")
            
        except Exception as err:
            print(err)
            self.browser.quit()
        
        try:
            self.logButton = self.browser.find_element_by_class_name("login_btn")
            self.logButton.click()
        except Exception as err:
            print(err)
            
        try:
            self.setButton = self.browser.find_element_by_class_name("nav-link")
            self.setButton.click()
        except Exception as err:
            print(err)
            
    
    
    def test_settings_form_input(self):
        
        form = self.browser.find_element_by_tag_name('h3').text,
        self.assertIn('LOGIN', form)
        
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')
        
        
        submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        
        username_input.send_keys('okay9')
        password_input.send_keys('working8')
        

        submit_btn.click()
        
        self.browser.find_element_by_class_name("nav-link").click()
        
        phone_input = self.browser.find_element_by_id("id_phone")
        email_input = self.browser.find_element_by_id("id_email")
        
        phone_input.send_keys('1234567890')
        email_input.send_keys('testing01@gmail.com')
        
        edit_btn = self.browser.find_element_by_class_name('btn-primary')
        edit_btn.click()
        # time.sleep(5)
        
        
    
   
   
    def test_settings_form_input_changes(self):
        
        form = self.browser.find_element_by_tag_name('h3').text,
        self.assertIn('LOGIN', form)
        
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')
        
        
        submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        
        
        username_input.send_keys('okay9')
        password_input.send_keys('working8')
        

        submit_btn.click()
        
        self.browser.find_element_by_class_name("nav-link").click()
        
        phone_input = self.browser.find_element_by_id("id_phone").clear()
        email_input = self.browser.find_element_by_id("id_email").clear()
        
        phone_input = self.browser.find_element_by_id("id_phone")
        email_input = self.browser.find_element_by_id("id_email")
        
        phone_input.send_keys('1234567890')
        email_input.send_keys('testing01@gmail.com')
        
        edit_btn = self.browser.find_element_by_class_name('btn-primary')
        edit_btn.click()
        
        back_btn = self.browser.find_element_by_class_name('btn-warning')
        back_btn.click()
        
        self.browser.find_element_by_class_name("nav-link").click()
       
       
       
    def test_settings_form_input_image(self):
        
        form = self.browser.find_element_by_tag_name('h3').text,
        self.assertIn('LOGIN', form)
        
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')
        
        
        submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        
        
        username_input.send_keys('okay9')
        password_input.send_keys('working8')
        

        submit_btn.click()
        
        self.browser.find_element_by_class_name("nav-link").click()
        
        image_input = self.browser.find_element_by_xpath("//input[@type='file']")
        
        image_input.send_keys("/Users/allyboy08/Pictures/test.jpg")
        
        
        edit_btn = self.browser.find_element_by_class_name('btn-primary')
        edit_btn.click()
        
        back_btn = self.browser.find_element_by_class_name('btn-warning')
        back_btn.click()
        
        self.browser.find_element_by_class_name("nav-link").click()
        
    
    
    
    