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


from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_browser_commands(driver):
    driver.get('https://opensource-demo.orangehrmlive.com')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    forgot_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-text.oxd-text--p.orangehrm-login-forgot-header')))
    forgot_login.click()

    reset_pass = wait.until( EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    clicked_ok = driver.find_element(By.CSS_SELECTOR, "p[class='oxd-text oxd-text--p']")
    if clicked_ok is not None:
        print("All good!")

    reset_pass = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    driver.back()
    login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    driver.forward()
    reset_pass = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    driver.refresh()
    reset_pass = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))




