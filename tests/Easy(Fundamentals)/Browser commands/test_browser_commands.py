"""
Test Case: Browser commands practice

This script tests the usage of browser commands with Selenium.

1. Opens the browser and navigates to the login page.
2. Clicks on the Forgot Password button.
3. Goes back to previous page.
4. Moves forward to next page.
5. Refreshes the page.

This test demonstrates:
- Basic browser commands interaction using Selenium

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get('https://opensource-demo.orangehrmlive.com')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(3)
clicked_ok = driver.find_element(By.CSS_SELECTOR, "p[class='oxd-text oxd-text--p']")
if clicked_ok is not None:
    print("All good!")

#time.sleep is NOT the best practice. Kept here for begginer reference!
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
driver.close()
