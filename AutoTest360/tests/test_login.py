import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        assert "inventory" in self.driver.current_url

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", "wrong_password")
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text or "Epic sadface" in error_text