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


class TestRegister(TransactionTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/Users/allyboy08/Downloads/chromedriver_win32/chromedriver")
        # self.browser.get("https://django-livecrm1.herokuapp.com/")
        self.browser.get("http://127.0.0.1:8000/login/?next=/")
        
    # def tearDown(self):
    #     self.browser.close()
        
    
    def test_register_with_correct_details(self):
        self.regLink = self.browser.find_element_by_class_name("ml-2")
        
        self.regLink.click()
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_username")))
            self.username.send_keys("okay10")
            self.email = self.browser.find_element_by_id("id_email")
            self.email.send_keys("testing00@gmail.com")
            self.password1 = self.browser.find_element_by_id("id_password1")
            self.password1.send_keys("working0")
            self.password2 = self.browser.find_element_by_id("id_password2")
            self.password2.send_keys("working0")
            
        except Exception as err:
            print(err)
            self.browser.quit()
        
        try:
            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)
        
        
    def test_register_with_existing_username(self):
        self.regLink = self.browser.find_element_by_class_name("ml-2")
        
        self.regLink.click()
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_username")))
            self.username.send_keys("okay9")
            self.email = self.browser.find_element_by_id("id_email")
            self.email.send_keys("testing01@gmail.com")
            self.password1 = self.browser.find_element_by_id("id_password1")
            self.password1.send_keys("working9")
            self.password2 = self.browser.find_element_by_id("id_password2")
            self.password2.send_keys("working9")
            
        except Exception as err:
            print(err)
            self.browser.quit()
        
        try:
            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)
        
    
    def test_register_with_no_details(self):
        self.regLink = self.browser.find_element_by_class_name("ml-2")
        
        self.regLink.click()
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_username")))
            self.username.send_keys("")
            self.email = self.browser.find_element_by_id("id_email")
            self.email.send_keys("")
            self.password1 = self.browser.find_element_by_id("id_password1")
            self.password1.send_keys("")
            self.password2 = self.browser.find_element_by_id("id_password2")
            self.password2.send_keys("")
            
        except Exception as err:
            print(err)
            self.browser.quit()
        
        try:
            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)
        
    
    
    def test_register_with_different_passwords(self):
        self.regLink = self.browser.find_element_by_class_name("ml-2")
        
        self.regLink.click()
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_username")))
            self.username.send_keys("okay0")
            self.email = self.browser.find_element_by_id("id_email")
            self.email.send_keys("testing01@gmail.com")
            self.password1 = self.browser.find_element_by_id("id_password1")
            self.password1.send_keys("working8")
            self.password2 = self.browser.find_element_by_id("id_password2")
            self.password2.send_keys("working1")
            
        except Exception as err:
            print(err)
            self.browser.quit()
        
        try:
            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)
        
    
    
    
    
        # time.sleep(20)

        # time.sleep(5)
        
        

        
       
    
    # def test_settings_form(self):
        
    #     form = self.browser.find_element_by_tag_name('h3').text,
    #     self.assertIn('LOGIN', form)
        
    #     username_input = self.browser.find_element_by_name('username')
    #     password_input = self.browser.find_element_by_name('password')
        
        
    #     submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        
    #     username_input.send_keys('okay8')
    #     password_input.send_keys('working7')
        

    #     submit_btn.click()
        
    #     self.browser.find_element_by_class_name("nav-link").click()
        
    #     phone_input = self.browser.find_element_by_id("id_phone")
    #     email_input = self.browser.find_element_by_id("id_email")
        
    #     phone_input.send_keys('1234567890')
    #     email_input.send_keys('testing9@gmail.com')
        
    #     edit_btn = self.browser.find_element_by_class_name('btn-primary')
    #     edit_btn.click()
    #     time.sleep(5)
        
    #     back_btn = self.browser.find_element_by_class_name('btn-warning')
    #     back_btn.click()
    
    
    
    
