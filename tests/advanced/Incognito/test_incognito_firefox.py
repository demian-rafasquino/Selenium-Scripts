from platform import android_ver

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.firefox.options import Options

#Chrome and firefox

@pytest.fixture
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture #fixture is like a setup helper. It's like "Hey, here's something I need for this test. clean it up afterwards"
def private_driver():
    options = Options()
    options.add_argument("-private")  # Open Firefox in private mode
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_incognito_firefox(private_driver):
    private_driver.get("https://the-internet.herokuapp.com/")
    main_site = WebDriverWait(private_driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".heading")))
    assert main_site.text == "Welcome to the-internet"
