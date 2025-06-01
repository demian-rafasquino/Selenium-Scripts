from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/horizontal_slider")
slider = browser.find_element(By.XPATH, "//input[@type='range']")
actions = ActionChains(browser)
actions.click_and_hold(slider).move_by_offset(50, 0).release().perform()
time.sleep(3)
browser.quit()
