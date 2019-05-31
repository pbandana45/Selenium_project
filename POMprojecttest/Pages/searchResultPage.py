from POMprojecttest.Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.common.exceptions import TimeoutException

class SearchresultPage():
    def __init__(self, driver):

        self.driver = driver
        self.selected_search_result_xpath = Locators.selected_search_result_xpath
        self.select_search_item_number = Locators.select_search_item_number
        self.title_of_selected_item = Locators.title_of_selected_item
        self.authors_xpath = Locators.authors_xpath
        self.number_of_customers_reviewed = Locators.number_of_customers_reviewed
        self.average_customer_review_stars = Locators.average_customer_review_stars
        self.list_of_book_editions_design1 = Locators.list_of_book_editions_design1
        self.list_of_book_editions_design2 = Locators.list_of_book_editions_design2

    ### Method to select a product from the list of products displayed
    def select_search_item_from_list(self):
        wait = WebDriverWait(self.driver, 10)
        result = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.selected_search_result_xpath)))[self.select_search_item_number].click()


    ### Method to get the Title of the product selected
    def get_item_title(self):
        wait = WebDriverWait(self.driver, 10)
        result = wait.until(EC.presence_of_element_located((By.XPATH, self.title_of_selected_item))).text
        print(" (1).. TITLE OF THE BOOK: " +result)


    ### Method to get the list of authors of the book selected
    def get_book_authors(self):
        wait = WebDriverWait(self.driver, 10)
        result = wait.until(EC.presence_of_element_located((By.XPATH, self.authors_xpath))).text
        print("  (2)..THE BOOK IS WRITTEN  " +result)


    ### Method to get the number of customers who reviewed thhe product
    def get_customer_ratings(self):
        try:
            #wait = WebDriverWait(self.driver, 10)
            result = self.driver.find_element_by_xpath(self.number_of_customers_reviewed).text
            print("  (3).. NUMBER OF CUSTOMERS REVIEWED THIS PRODUCT: " +result)
        except NoSuchElementException:
            print("  (3).. NO CUSTOMER REVIEWED THIS PRODUCT")


    ### Method to get the average number of stars given by customers to the product
    def get_average_customer_review_stars(self):
        #wait = WebDriverWait(self.driver, 10)
        try:

            result = self.driver.find_element_by_xpath(self.average_customer_review_stars).text
            print("  (4).. AVERAGE CUSTOMER STARS " +result)

        except NoSuchElementException:
            print("  (4).. NO CUSTOMER REVIEW STARS FOR THIS PRODUCT")



    ### Method to get the book edition and its price
    def get_book_edition_and_price(self):
        #wait = WebDriverWait(self.driver, 10)

                                ############## DESIGN #1  ##############

        try:

            edition_list_design1 = self.driver.find_elements_by_xpath(self.list_of_book_editions_design1)
            length_of_edition_list_design1 = len(edition_list_design1)
            i = 0
            for i in range(length_of_edition_list_design1):

                edition_design1 = self.driver.find_element_by_xpath("//*[@id='mediaTab_heading_" + str(i) + "']/a/span/div[1]/span").text
                edition_price_design1 = self.driver.find_element_by_xpath("//*[@id='mediaTab_heading_" + str(i) + "']/a/span/div[2]/span").text
                if edition_design1 == 'Other Sellers':
                    exit(0)
                print("  (5).. BOOK EDITION " + edition_design1 + "  HAS PRICE:  " + edition_price_design1)


        except ElementNotVisibleException:
            pass
        except NoSuchElementException:
            pass
        except SystemExit:
            pass
        except TimeoutException:
            print("TimeoutException!!!")

                                ############### DESIGN #2  ################

        try:
            edition_list_design2 = self.driver.find_elements_by_xpath(self.list_of_book_editions_design2)
            length_of_edition_list_design2 = len(edition_list_design2)
            i = 1
            for i in range(length_of_edition_list_design2):
                i = i + 1

                edition_design2 = self.driver.find_element_by_xpath("//*[@id='tmmSwatches']/ul/li[" +str(i)+ "]/span/span/span/a/span").text
                edition_price_design2 = self.driver.find_element_by_xpath("//*[@id='tmmSwatches']/ul/li[" +str(i)+ "]/span/span/span/a/span/span").text
                print("  (5) .. BOOK EDITION:  " + edition_design2 + "  HAS PRICE: " + edition_price_design2)


        except ElementNotVisibleException:
            pass
        except NoSuchElementException:
            pass
        except TimeoutError:
            print("TimeoutException!!!")


    ### Method to get the product details and features
    def get_product_details(self):
                            ######### Design #1 ##########
        try:
            edition_list_design1 = self.driver.find_elements_by_xpath(self.list_of_book_editions_design1)
            length_of_edition_list_design1 = len(edition_list_design1)
            i = 0
            for i in range(length_of_edition_list_design1):
                click_edition = self.driver.find_element_by_xpath("//*[@id='mediaTab_heading_" + str(i) + "']/a/span").click()
                edition_design1 = self.driver.find_element_by_xpath("//*[@id='mediaTab_heading_" + str(i) + "']/a/span/div[1]/span").text
                if edition_design1 == 'Other Sellers':
                    exit(0)
                product_details_design2 = self.driver.find_element_by_xpath('//*[@id="productDetailsTable"]/tbody/tr/td/div').text
                print("  (6).. PRODUCT DETAILS FOR EDITION: " +edition_design1+ "------->" +product_details_design2)

        except ElementNotVisibleException:
            pass

        except NoSuchElementException:
            pass
        except SystemExit:
            pass
        except TimeoutException:
            print("TimeoutException!!!")

                                    ######### Design #2 ##########
        try:
            edition_list_design2 = self.driver.find_elements_by_xpath(self.list_of_book_editions_design2)
            length_of_edition_list_design2 = len(edition_list_design2)
            i = 1
            for i in range(length_of_edition_list_design2):
                i = i + 1
                click_edition_design2 = self.driver.find_element_by_xpath("//*[@id='tmmSwatches']/ul/li[" + str(i) + "]/span/span/span")
                edition_design2 = self.driver.find_element_by_xpath("//*[@id='tmmSwatches']/ul/li[" + str(i) + "]/span/span/span/a/span").text
                product_details_design2 = self.driver.find_element_by_xpath('//*[@id="productDetailsTable"]/tbody/tr/td/div').text
                print("  (6).. PRODUCT DETAILS FOR EDITION: " +edition_design2+ "------->" + product_details_design2)

        except ElementNotVisibleException:
            pass
        except NoSuchElementException:
            pass
        except TimeoutError:
            print("TimeoutException!!!")
