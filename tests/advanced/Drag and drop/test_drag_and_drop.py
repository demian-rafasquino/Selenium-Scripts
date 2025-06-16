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

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_drag_and_drop(driver):
    driver.get("https://demoqa.com/droppable")

    # Item to drag and destination
    item_to_drag = driver.find_element(By.ID, "draggable")
    destination = driver.find_element(By.ID, "droppable")

    # Action chains
    actions = ActionChains(driver)

    # Using action chains to drag and drop
    actions.drag_and_drop(item_to_drag, destination).perform()
    dropped = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='simpleDropContainer'] p")))
    assert dropped.text == "Dropped!"
