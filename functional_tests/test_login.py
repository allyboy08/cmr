from selenium import webdriver
from accounts.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestLogin(StaticLiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/allyboy08/Downloads/chromedriver_win32/chromedriver')
        
    def tearDown(self):
        self.browser.close()