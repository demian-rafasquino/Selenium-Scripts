# tests/conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver  # This gives control back to the test using the fixture
    driver.quit()  # After the test finishes, quit the browser