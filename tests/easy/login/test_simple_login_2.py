"""
Test Case: Login Functionality - Practice Automation website

This script tests the login functionality of the Practice automation web application.
Steps:
1. Opens the browser and navigates to the login page.
2. Enters valid credentials (student / Password123).
3. Clicks the login button.
4. Verifies that the login was successful by asserting the presence of "Logged in successful".

This test demonstrates:
- Basic field interaction using Selenium
- Attribute validation before clicking
- Post-login assertion to confirm navigation
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_2(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Creation of username and password variables
    username = "student"
    password = "Password123"

    # username and password fields
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Sending information to username and password fields
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Finding login button and clicking
    driver.find_element(By.ID, "submit").click()

    # Asserting it logged in correctly by finding logout button
    logged_in = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".wp-block-button__link.has-text-color.has-background.has-very-dark-gray-background-color")))
    assert logged_in.text == "Log out"




