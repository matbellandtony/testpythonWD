import time
import urllib

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from elements.test_elements import *
from elements.product_elements import *
from locators import Exampleofalocator
from pages.page import Page
