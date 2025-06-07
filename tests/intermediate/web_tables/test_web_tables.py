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

from selenium.webdriver.common.by import By

def test_web_tables(driver):
    driver.get('https://cosmocode.io/automation-practice-webtable')

    # Scroll table into view (more flexible than hardcoding)
    table = driver.find_element(By.ID, 'countries')
    driver.execute_script("arguments[0].scrollIntoView();", table)

    # Get rows and count them (excluding header)
    rows = table.find_elements(By.TAG_NAME, 'tr')
    row_count = len(rows) - 1  # Minus one to exclude the header
    print(f"Total data rows: {row_count}")

    # Search for a specific value
    target_value = 'Argentina'
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

