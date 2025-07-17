from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart = (By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
        self.view_cart = (By.XPATH, "//a[contains(text(),'View Cart')]")

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()
        self.driver.find_element(*self.view_cart).click()