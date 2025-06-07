"""
Test Case: Broken Images

This script tests all images on a website and returns the broken ones with a status that is not 200

1. Opens the browser and navigates to the website
2. Gets the response status code.
3. Adds the ones with status different from 200 to the empty list
4. Reports broken images
5. Reports a list of broken images links

This test demonstrates:
- Broken images handling with Selenium

"""

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()

#Find all images
images = browser.find_elements(By.TAG_NAME, "img")
broken_images = []

#Checking the broken ones and apending them to an empty list
for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken image Found")

#Reporting the broken images found
if broken_images:
    print("list of broken images:")
    for broken_images in broken_images:
        print(broken_images)
else:
    print("No broken images found.")

browser.quit()