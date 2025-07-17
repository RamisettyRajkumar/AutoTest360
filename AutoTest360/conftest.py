import pytest
from selenium import webdriver

@pytest.fixture
def setup_and_teardown(request):
    driver = webdriver.Chrome()  # Or Firefox(), Edge(), etc.
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")  # Base URL of your website

    request.cls.driver = driver  # Attach driver to test class

    yield  # Test will run here

    driver.quit()  # Close browser after test