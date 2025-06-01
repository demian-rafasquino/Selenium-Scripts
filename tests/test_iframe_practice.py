from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.automationtesting.co.uk/iframes.html')
iframe = browser.find_element(By.CSS_SELECTOR, 'iframe[src="https://www.youtube.com/embed/jNQXAC9IVRw"]')
browser.switch_to.frame(iframe)
video = browser.find_element(By.ID, "movie_player")
video.click()
time.sleep(4)
browser.switch_to.default_content()
browser.find_element(By.CSS_SELECTOR, "a[class='logo'] strong").click()
browser.quit()