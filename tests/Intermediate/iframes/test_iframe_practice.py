"""
Test Case: iframes handling

This script tests the handling of iframes

1. Opens the browser and navigates to a website
2. Finds a specific iframe.
3. Switches to iframe
4. Performs an action inside the iframe
5. Switches back to default content
6. Performs an action on the default content(outside of iframe)

This test demonstrates:
- Finding and Switching to Iframe
- Performance of a specific task inside iframe
- Switching back to broader webpage

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://practice-automation.com/iframes/")

#Find specific iframe
second_iframe = browser.find_element(By.ID, "iframe-2")

#Switch to iframe
browser.switch_to.frame(second_iframe)

#Find element inside iframe (Selenium webdriver link in this case, for example)
browser.find_element(By.XPATH, "//iframe[@id='iframe-2']").click()
time.sleep(3)

#Switch back to regular page and scroll up.
browser.switch_to.default_content()
driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

#Check we are at the top
home_link = browser.find_element(By.XPATH, "//a[normalize-space()='Home']")
assert home_link.is_displayed()

browser.quit()