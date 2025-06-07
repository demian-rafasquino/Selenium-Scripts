"""
Test Case: Handling web tables

This script tests the handling of web tables with Selenium

1. Opens the browser and navigates to a website
2. Scrolls to the table.
3. Reports amount of rows (Excluding header)
4. Searches a specific value and prints it

This test demonstrates:
- Basic counting of web table rows
- Specific value search

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('https://cosmocode.io/automation-practice-webtable')
browser.maximize_window()


table = browser.find_element(By.ID, 'countries')
browser.execute_script("arguments[0].scrollIntoView();", table)


rows = table.find_elements(By.TAG_NAME, 'tr')
row_count = len(rows) - 1
print(f"Total data rows: {row_count}")


target_value = 'Wakanda'
found = False
for row in rows[1:]:  # Skip header
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        if target_value in cell.text:
            print(f"Found value '{target_value}'")
            found = True
            break
    if found:
        break

if not found:
    print(f"Target value '{target_value}' not found")


browser.quit()