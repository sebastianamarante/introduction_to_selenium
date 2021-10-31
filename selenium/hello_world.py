import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # prepara el entorno de la prueba
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):  # serie de acciones
        driver = self.driver
        driver.get('https://www.platzi.com')
        driver.implicitly_wait(10)

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):  # acciones para finalizar
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))
