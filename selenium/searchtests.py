import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchTests(unittest.TestCase):

    def setUp(self):  # prepara el entorno de la prueba
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a/img')
        self.assertEqual(1, len(products))

    def test_demo_store(self):  # serie de acciones
        pass

    def tearDown(self):  # acciones para finalizar
        self.driver.quit()
