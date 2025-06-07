#INVALID TEST. WEBSITE DOESN'T ALLOW TO SEND KEYS INTO THE TEXT EDITOR ANYMORE.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/iframe')

#Find the iframe
iframe = browser.find_element(By.ID, 'mce_0_ifr')

#Switch to iframe
browser.switch_to.frame(iframe)

#Find the text editor and send keys
text_editor = browser.find_element(By.ID, 'tinymce')
text_editor.clear()
text_editor.send_keys('Trying to write inside the editor on an iframe')

#Switch back to the website, click a link and exit
browser.switch_to.default_content()
link_outside_iframe = browser.find_element(By.XPATH, '//a[normalize-space()="Elemental Selenium"]')
link_outside_iframe.click()
time.sleep(3)
browser.quit()