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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkboxes(driver):
    driver.get('https://productbuilder.rednao.com/product/checkbox-demo/')
    driver.maximize_window()
    driver.execute_script('window.scrollTo(0, 0);')

    wait = WebDriverWait(driver, 10)

    # Wait for and click the checkbox once
    checkbox_1 = wait.until(EC.element_to_be_clickable((By.ID, 'field_2_2')))
    checkbox_1.click()

    # Wait for it to be clickable again before unchecking
    checkbox_1 = wait.until(EC.element_to_be_clickable((By.ID, 'field_2_2')))
    checkbox_1.click()

    # Wait until at least one checkbox is present before selecting all
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    # Check them all using the space key
    for checkbox in checkboxes:
        checkbox.send_keys(Keys.SPACE)

    checked_count = 0

    for checkbox in checkboxes:
        if checkbox.is_selected():
            checked_count += 1

    expected_checked_count = 9

    assert checked_count == expected_checked_count, f"Expected {expected_checked_count} checkboxes, but found {checked_count}."
    print('✅ Checkbox count verified')

