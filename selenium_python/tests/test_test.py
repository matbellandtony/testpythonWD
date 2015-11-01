from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from seleniumfoundation.config import get_config
from seleniumfoundation.testcase import SeleniumGridTestCase

from factory.test_factory import TestFactory
from locators import Exampleofalocator
from pages.test_page import TestPage

class TestTest(SeleniumGridTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.app_url)
        self.AP = TestPage(self.driver)
        self.authenticate(self.driver, self.user_id, self.username)
        self.Test_factory = TestFactory(self.driver)

    def tearDown(self):
        self.driver.quit()
