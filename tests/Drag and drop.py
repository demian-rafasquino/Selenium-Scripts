from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://demoqa.com/droppable")
item_to_drag = browser.find_element(By.ID, "draggable")
destination = browser.find_element(By.ID, "droppable")
actions = ActionChains(browser)
actions.drag_and_drop(item_to_drag, destination).perform()
time.sleep(3)
browser.quit()