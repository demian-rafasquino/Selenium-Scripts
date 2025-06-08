from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
url = "https://demo.automationtesting.in/Resizable.html"
driver.get(url)
resize = driver.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")

#Finding the current size of the element
initial_resizable_element = driver.find_element(By.XPATH, "//div[@id='resizable']")
initial_size = initial_resizable_element.size
print("Initial size: ", initial_size)
time.sleep(4)
action_chains = ActionChains(driver)
action_chains.click_and_hold(resize).move_by_offset(100, 100).release().perform()
time.sleep(2)
#Now to check the new size
resized_element = initial_resizable_element.size
print("Resized Element: ", resized_element)