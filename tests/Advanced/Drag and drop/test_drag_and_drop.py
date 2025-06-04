"""
Test Case: Drag and Drop

This script tests how to handle drag and drop functionality

1. Opens the browser and navigates to a website with a draggable item and a drop field
2. Creates a variable with the item to be dragged and another with its destination
3. Drags the draggable item to the destination and drops it


This test demonstrates:
- Action chains
- Drag and drop action


"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://demoqa.com/droppable")

#Item to drag and destination
item_to_drag = browser.find_element(By.ID, "draggable")
destination = browser.find_element(By.ID, "droppable")

#Action chains
actions = ActionChains(browser)

#Using action chains to drag and drop
actions.drag_and_drop(item_to_drag, destination).perform()
time.sleep(3)
browser.quit()