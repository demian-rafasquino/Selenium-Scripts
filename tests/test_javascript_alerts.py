#This is about how to handle those notifications that appear on pages over the website.
# They are javascript and don't allow the user to interact with the site

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"

browser.get(url)
js_alert = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
js_alert.click()

#Now that I triggered the alert, now we handle it by switching to it
alert =browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(3)
#Now we click on the OK

alert.accept()

#alert with confirmation. I'm going to click the cancel button on this one
time.sleep(2)
js_confirm = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
js_confirm.click()

confirm = browser.switch_to.alert
confirm_text = confirm.text
print(confirm_text)
time.sleep(2)
confirm.dismiss()
time.sleep(2)
#Now the prompt! On this one, I have to enter a text to keep going/close the alert

js_prompt = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
js_prompt.click()
time.sleep(2)
prompt = browser.switch_to.alert
prompt_text = prompt.text
print(prompt_text)

alert.send_keys("Demián")
time.sleep(2)
alert.accept()
time.sleep(2)

browser.quit()