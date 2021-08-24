# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from django.contrib.auth.models import User

# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.urls import reverse
# import time


# class TestLogin(StaticLiveServerTestCase):
    
#     def setUp(self):
#         self.browser = webdriver.Chrome('/Users/allyboy08/Downloads/chromedriver_win32/chromedriver')
        
        
#     def tearDown(self):
#         self.browser.close()
        
    
        
    # def test_login_form(self):
    #     self.browser.get(self.live_server_url)
        
    #     form = self.browser.find_element_by_tag_name('h3').text,
    #     self.assertIn('LOGIN', form)
        
    #     username_inputbox = self.browser.find_element_by_name('username')
    #     self.assertEqual(
    #         username_inputbox.get_attribute('placeholder'),
    #         'Username...'
    #     )
    
    #     password_inputbox = self.browser.find_element_by_name('password')
    #     self.assertEqual(
    #         password_inputbox.get_attribute('placeholder'),
    #         'Password...'
    #     )
        
    #     submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        
    #     username_inputbox.send_keys('testsss')
    #     password_inputbox.send_keys('qwerty4321')
    #     # self.browser.find_element_by_xpath('//input[@value="Login"]').click()
        
       
    #     submit_btn.click()
        
    #     time.sleep(10)
       
        # path = urlparse(self.browser.current_url).path
        # self.assertEqual('/', path)
        
        
   
        
        
        
        
   
    
    # def test_sign_up_link_redirects_to_sign_up_page(self):
    #     self.browser.get(self.live_server_url)
        
        
    #     register_url = self.live_server_url + reverse('register')
    #     self.browser.find_element_by_tag_name('a').click()
    #     self.assertEquals(
    #         self.browser.current_url,
    #         register_url
    #     )
    
    
        #  self.browser.find_element_by_id("id-register").click()

        # username = "newuser"
        # self.browser.find_element_by_id("id_username").send_keys(username)
        # self.browser.find_element_by_id("id_email").send_keys("newuser@email.com")
        # self.browser.find_element_by_id("id_password1").send_keys("Psiph5sK")
        # self.browser.find_element_by_id("id_password2").send_keys("Psiph5sK")

        # self.browser.find_element_by_id("user-registration-submit").click()
        # self.assertEqual(username, self.browser.find_element_by_id("username-text").text)
        
    # def test_user_is_redirected_to_register_page(self):
        
    #     self.browser.get(self.live_server_url)
    #     register_url = self.live_server_url + reverse('register')
    #     self.browser.find_element_by_tag_name('a').click()
    #     self.assertEquals(
    #         self.browser.current_url,
    #         register_url
    #     )
    
        
       
        
    #     self.browser.find_element_by_id("id_username").send_keys("okay1"),
    #     self.browser.find_element_by_id("id_email").send_keys("testing4@gmail.com"),
    #     self.browser.find_element_by_id("id_password1").send_keys("working2"),
    #     self.browser.find_element_by_id("id_password2").send_keys("working2")
        
        
    #     submit_btn = self.browser.find_element_by_class_name('login_btn')
    #     submit_btn.click()
        # login_url = self.live_server_url + reverse('login')
        
        # login_url = self.live_server_url + reverse('login')
        # self.assertEquals(

        #     self.browser.find_element_by_tag_name('h3').text,
        #     'LOGIN'
        # )
    #     time.sleep(20)
        
        
        
      
    
        
        
    
        
    
from django.test.testcases import TransactionTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts.models import Customer
from accounts.forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestLogin(TransactionTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/Users/allyboy08/Downloads/chromedriver_win32/chromedriver")
        self.browser.get("https://django-livecrm1.herokuapp.com/")
        
    
    def test_register_and_login(self):
        self.regLink = self.browser.find_element_by_class_name("ml-2")
        
        self.regLink.click()
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_username")))
            self.username.send_keys("okay5")
            self.email = self.browser.find_element_by_id("id_email")
            self.email.send_keys("testing8@gmail.com")
            self.password1 = self.browser.find_element_by_id("id_password1")
            self.password1.send_keys("working6")
            self.password2 = self.browser.find_element_by_id("id_password2")
            self.password2.send_keys("working6")
            
        except Exception as err:
            print(err)
            self.browser.quit()
        
        try:
            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)
        
        # time.sleep(20)

        form = self.browser.find_element_by_tag_name('h3').text,
        self.assertIn('LOGIN', form)
        
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')
        
        
        submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        
        username_input.send_keys('okay5')
        password_input.send_keys('working6')
        
        
       
        submit_btn.click()
        
        time.sleep(5)
        
    def test_settings(self):
        
        form = self.browser.find_element_by_tag_name('h3').text,
        self.assertIn('LOGIN', form)
        
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')
        
        
        submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        
        username_input.send_keys('okay5')
        password_input.send_keys('working6')
        

        submit_btn.click()
        
        self.browser.find_element_by_class_name("nav-link").click()
        
        time.sleep(10)
    
    