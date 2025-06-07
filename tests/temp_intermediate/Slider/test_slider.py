"""
Test Case: Slider

This script tests how to handle using a slider through Selenium

1. Opens the browser and navigates to a website with a slider
2. Grabs the slider by clicking and holding
3. Drags the slider to a specified input
4. Repeats


This test demonstrates:
- Click and hold actions
- Drag action by offset


"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/horizontal_slider")

#Finding slider
slider = browser.find_element(By.XPATH, "//input[@type='range']")

actions = ActionChains(browser)

#Action chain to click and hold, then slide by offset
actions.click_and_hold(slider).move_by_offset(50, 0).release().perform()
time.sleep(3)
actions.click_and_hold(slider).move_by_offset(25, 0).release().perform()
time.sleep(3)

#If the offset is more than the slider has, it just goes to the top
actions.click_and_hold(slider).move_by_offset(500, 0).release().perform()
time.sleep(3)

browser.quit()