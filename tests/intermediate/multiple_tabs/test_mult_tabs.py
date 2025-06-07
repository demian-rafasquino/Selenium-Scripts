"""
Test Case: Handling multiple tabs and windows

This script tests the handling of multiple tabs and windows with Selenium

1. Opens the browser and navigates to a website
2. opens a new tab and navigates to a different website
3. Reports total amount of tabs
4. Reports the value of each tab
5. Reports the value of the current tab
6. Clicks on an element.
7. Goes back to first tab.
8. Clicks on an element on the first tab

This test demonstrates:
- Opening of new tabs.
- Changing from one tab to another

"""

from selenium.webdriver.common.by import By
import time

def test_mult_tabs(driver):
    driver.get("https://www.selenium.dev/")
    driver.switch_to.new_window()
    driver.get("https://playwright.dev/")

    # Print number of tabs
    number_of_tabs = len(driver.window_handles)
    print(number_of_tabs)

    # Get values for tabs
    tabs_value = driver.window_handles
    print(tabs_value)

    # Print current tab value
    current_tab = driver.current_window_handle
    print(current_tab)
    time.sleep(3)

    # Clicking on an element
    driver.find_element(By.CSS_SELECTOR, '.getStarted_Sjon').click()
    time.sleep(4)

    # Switching back to the first tab
    first_tab = driver.window_handles[0]

    # This commented code is another way to do it by using an if.
    # if current_tab != first_tab:
    #     browser.switch_to.window(first_tab)

    driver.switch_to.window(first_tab)

    # Clicking on a link on the first tab.
    driver.find_element(By.XPATH, '//span[normalize-space()="Downloads"]').click()

