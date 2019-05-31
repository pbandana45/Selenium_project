from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from POMprojecttest.Pages.homePage import HomePage
from POMprojecttest.Pages.searchResultPage import SearchresultPage
from POMprojecttest.Locators.locators import Locators
import HtmlTestRunner


class amazonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\Users\bpradhan\Downloads\chromedriver_win32\chromedriver.exe')
        cls.driver.maximize_window()
        wait = WebDriverWait(cls.driver,10)

### Calls different methods from different classes
    def test_search(self):
        driver = self.driver
        driver.get("https://www.amazon.com/")
        wait = WebDriverWait(driver, 10)

        home = HomePage(driver)
        ### Calls method that selects a product from the search dropdown
        home.searcselect_fromDropdown()
        ### Calls method that lets you enter a text in the search textbox
        home.enter_search_text(Locators.enter_search_text)

        time.sleep(2)


        search = SearchresultPage(driver)
        time.sleep(5)
        ### Calls method that lets you select a product from the list of search results
        search.select_search_item_from_list()
        time.sleep(5)
        ### Calls method that gets the title of the product selected
        search.get_item_title()
        time.sleep(5)
        ### Calls method that gets the list of authors of the book selected
        search.get_book_authors()
        time.sleep(20)
        ### calls a method that grabs the number of customers who rated the product
        search.get_customer_ratings()
        time.sleep(3)
        ### Calls a method that gets the average rating stars given to the product
        search.get_average_customer_review_stars()
        time.sleep(3)
        ### Calls a method that grabs the book edition along with its price
        search.get_book_edition_and_price()
        time.sleep(3)
        ### calls a method that gets the product details
        search.get_product_details()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/bpradhan/PycharmProjects/Selenium_project/Reports'))


