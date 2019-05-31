from POMprojecttest.Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import sys

class HomePage():
    def __init__(self, driver):

        self.driver = driver
        self.searchAll_Dropdown_xpath = Locators.searchAll_Dropdown_xpath
        self.chooseFromDropdown_Books_xpath = Locators.chooseFromDropdown_Books_xpath
        self.search_textBox_xpath = Locators.search_textBox_xpath
        self.search_button_xpath = Locators.search_button_xpath


    #####Method to select a product from the search dropdown.
    def searcselect_fromDropdown(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.searchAll_Dropdown_xpath))).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.chooseFromDropdown_Books_xpath))).click()


    #### Method to enter a text in the search textbox and search the same
    def enter_search_text(self, enter_search_text):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element_by_xpath(self.search_textBox_xpath).clear()
        wait.until(EC.presence_of_element_located((By.XPATH, self.search_textBox_xpath))).send_keys(enter_search_text)
        wait.until(EC.presence_of_element_located((By.XPATH, self.search_button_xpath))).click()



