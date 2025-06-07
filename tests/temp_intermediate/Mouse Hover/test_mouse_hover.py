"""
Test Case: Mouse hover

This script tests how to hover the mouse to show non visible options on the site with Selenium

1. Opens the browser and navigates to a website
2. Hovers the mouth other an option to show the hidden options
3. Clicks on one of the hidden options once they become visible through the hover action


This test demonstrates:
- Hover action over web elements to show non visible options
- Clicking on said non visible options once they become visible


"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

#Can't click on the element that only appears when hovering the mouse over a place.
# If I try, it gives an error because the element is present but not interactable
#Using action chains. They can automate low level interactions like mouse movement, mouse buttons, key press and context menu interactions


actions = ActionChains(browser)
hover_element = browser.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
time.sleep(3)
actions.move_to_element(hover_element).perform()
time.sleep(3)
browser.find_element(By.CSS_SELECTOR, "a[href='Frames.html']").click()

browser.quit()