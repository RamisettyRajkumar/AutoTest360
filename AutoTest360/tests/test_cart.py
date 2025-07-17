import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.cart_page import CartPage

@pytest.fixture(scope="function")
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup_and_teardown")
class TestCart:

    def test_add_item_to_cart(self):
        login_page = LoginPage(self.driver)
        cart_page = CartPage(self.driver)

        login_page.login("standard_user", "secret_sauce")
        cart_page.add_item_to_cart("Sauce Labs Backpack")
        assert cart_page.is_item_in_cart("Sauce Labs Backpack")

    def test_remove_item_from_cart(self):
        login_page = LoginPage(self.driver)
        cart_page = CartPage(self.driver)

        login_page.login("standard_user", "secret_sauce")
        cart_page.add_item_to_cart("Sauce Labs Backpack")
        cart_page.remove_item_from_cart("Sauce Labs Backpack")
        assert not cart_page.is_item_in_cart("Sauce Labs Backpack")