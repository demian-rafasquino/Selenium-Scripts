"""
Test Case: Simple Date Picker

This script tests the handling of simple date pickers

1. Opens the browser and navigates to a website with a simple date picker
2. Clicks on the date picker to open it
3. Switches to the iframe of the date picker
4. Creates a variable with the current date in case it was needed to manipulate the used date in other tests
5. Creates variable for the date format
6. Sends date as text into the date field on the date picker



This test demonstrates:
- Handling of a simple date picker
- Creation of variables for current date and date format
- Sending information to a date picker

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta


browser = webdriver.Firefox()
browser.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)

#Closing the warning above it
browser.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()

#Now, interacting with the date picker
date_picker_iframe = browser.find_element(By.CSS_SELECTOR, ".demo-frame.lazyloaded")
browser.switch_to.frame(date_picker_iframe)


simple_date_picker = browser.find_element(By.ID, "datepicker")
simple_date_picker.click()
time.sleep(2)

#Now, the date picker is open. Selecting current date
current_date = datetime.now()
formatted_date = current_date + timedelta(days=1)#This will add 1 day to the current day. If it's the 15th now, it will select the 16th
#You can say -2 if you want the date to be in the past.

#Making sure the format is correct
# In this case, the format is mm/dd/yyyy

date_format = formatted_date.strftime("%m/%d/%y")

#If I inspect the field that gets filled when selecting the date, we can see it's a text type.
# So I can actually just send the date we want.

browser.find_element(By.CSS_SELECTOR, "#datepicker").send_keys(date_format + Keys.TAB)#After sending a date, I need to click tab on the keyboard on this particular date picker. Although enter works too according to my testing
time.sleep(3)

browser.quit()

