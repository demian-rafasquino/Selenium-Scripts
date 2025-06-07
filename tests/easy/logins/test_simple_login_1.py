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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"

driver.get(login_url)

#Finding the correct fields
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")

#Sending the information stored on the variables
username_field.send_keys(username)
password_field.send_keys(password)

#Find and click login button
login_button = driver.find_element(By.ID, "login-button")
assert not login_button.get_attribute("disabled")#This is to check that the button is not disabled. It looks for the atribute disabled and asserts it's not there.
login_button.click()
time.sleep(5)

#Checking it worked by asserting an element on the page that comes after the click
success_element = driver.find_element(By.CSS_SELECTOR, ".title")
assert success_element.text == "Products"