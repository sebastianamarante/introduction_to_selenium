import unittest
from selenium import webdriver
from time import sleep


class TestingMercadoLibre(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('AR')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        try:
            cookies_button = driver.find_element_by_xpath("//button[@id='newCookieDisclaimerButton']")
            cookies_button.click()
        except:
            pass

        condition = driver.find_element_by_xpath("//span[contains(text(),'Nuevo')]")
        condition.click()
        sleep(3)

        order_menu = driver.find_element_by_css_selector('.andes-dropdown__trigger > span')
        order_menu.click()

        higher_price = driver.find_element_by_css_selector(
            'a.andes-list__item:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []
        tries = 1

        for i in range(5):
            if tries == 1:
                article_name = driver.find_element_by_xpath(f"/html/body/main/div/div[1]/section/ol/li[1]/div/div/div[2]/div[2]/a/h2").text
                articles.append(article_name)
                article_price = driver.find_element_by_xpath(f"/html/body/main/div/div[1]/section/ol/li[1]/div/div/div[2]/div[3]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]")
                prices.append(article_price)
                tries += 1
                i = 1
                return i
            else:
                article_name = driver.find_element_by_xpath(f"/html/body/main/div/div[1]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2")
                article_price = driver.find_element_by_xpath(f"/html/body/main/div/div[1]/section/ol/li[{i + 1}]]/div/div/div[2]/div[2]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]")
                prices.append(article_price)
                articles.append(article_name)
                print(articles, prices)

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
