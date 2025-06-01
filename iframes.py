
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/iframe')

iframe = browser.find_element(By.ID, 'mce_0_ifr')
browser.switch_to.frame(iframe)

text_editor = browser.find_element(By.ID, 'tinymce')
text_editor.clear()
text_editor.send_keys('Trying to write inside the editor on an iframe')

browser.switch_to.default_content()
link_outside_iframe = browser.find_element(By.XPATH, '//a[normalize-space()="Elemental Selenium"]')
link_outside_iframe.click()