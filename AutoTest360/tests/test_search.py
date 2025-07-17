import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_search_for_product(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        # After login, all products will be listed
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        # Check if any product name contains "Backpack"
        found = any("Backpack" in product.text for product in products)
        assert found, "Backpack product not found"