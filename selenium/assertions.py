import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionTests(unittest.TestCase):

    def setUp(self):  # prepara el entorno de la prueba
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_test_field(self):
        self.assertTrue(self.is_element_present(By.ID, "q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    def test_demo_store(self):  # serie de acciones
        pass

    def tearDown(self):  # acciones para finalizar
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by= how, value=what)
        except NoSuchElementException as variable:
            return False
        return True