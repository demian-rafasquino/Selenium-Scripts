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

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://www.automationtesting.co.uk/iframes.html")
time.sleep(2)
second_iframe = browser.find_element(By.CSS_SELECTOR, "iframe[src='https://www.youtube.com/embed/jNQXAC9IVRw']")

browser.switch_to.frame(second_iframe)
time.sleep(2)
browser.find_element(By.ID, "movie_player").click()
time.sleep(3)
browser.quit()