"""
Test Case: Login Functionality - SauceDemo

This script tests the login functionality of the SauceDemo web application.
Steps:
1. Opens the browser and navigates to the login page.
2. Enters valid credentials (standard_user / secret_sauce).
3. Clicks the login button.
4. Verifies that the login was successful by asserting the presence of the "Products" title on the landing page.

This test demonstrates:
- Basic field interaction using Selenium
- Attribute validation before clicking
- Post-login assertion to confirm navigation
"""

from selenium.webdriver.common.by import By
import time


from selenium.webdriver.common.by import By
import time

def test_login(driver):
    """
    Test that a user can log in successfully on the SauceDemo site.
    """
    username = "standard_user"
    password = "secret_sauce"
    login_url = "https://www.saucedemo.com/"

    driver.get(login_url)

    # Locate and fill in username and password
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Click the login button and assert it is enabled
    login_button = driver.find_element(By.ID, "login-button")
    assert not login_button.get_attribute("disabled")
    login_button.click()

    time.sleep(3)  # Optional: Replace with WebDriverWait in next steps

    # Assert that the user is redirected to the Products page
    assert driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"



