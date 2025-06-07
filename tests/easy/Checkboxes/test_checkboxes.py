"""
Test Case: Checkboxes

This script tests the checking of checkboxes on a website with options
1. Opens the browser and navigates to the website
2. Checks and unchecks one checkbox
3. Checks all checkboxes at the same time.
4. Closes the browser.

This test demonstrates:
- Basic checkbox interaction.
- Way to check all checkboxes at once.
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_checkboxes(driver):
    driver.get('https://productbuilder.rednao.com/product/checkbox-demo/')
    driver.maximize_window()
    driver.execute_script('window.scrollTo(0, 0);')

    # Checking and unchecking one.
    driver.find_element(By.ID, 'field_2_2').click()
    time.sleep(3)
    driver.find_element(By.ID, 'field_2_2').click()

    # Checking them all at once.

    checkboxes = driver.find_elements(By.XPATH, "//input[@type= 'checkbox']")
    for checkbox in checkboxes:
        checkbox.send_keys(Keys.SPACE)  # Using spacebar to check them

    checked_count = 0

    for checkbox in checkboxes:
        if checkbox.is_selected():
            checked_count += 1

    expected_checked_count = 9

    if checked_count == expected_checked_count:
        print('Checkbox count verified')
    else:
        print('Checkbox count missmatch')
    time.sleep(5)

