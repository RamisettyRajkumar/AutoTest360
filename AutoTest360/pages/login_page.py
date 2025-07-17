# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def _init_(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
        wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()