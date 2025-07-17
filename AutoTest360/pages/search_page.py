from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.ID, "search_product")
        self.search_button = (By.ID, "submit_search")

    def search_product(self, product_name):
        self.driver.find_element(*self.search_input).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()