"""
Test Case: Dropdown Date Picker

This script tests the handling of simple droppdown date pickers

1. Opens the browser and navigates to a website with a dropdown date picker
2. Clicks on the date picker to opens it
3. Creates variable for current date, day, month and year
4. Selects options on both dropdowns for month and year




This test demonstrates:
- Handling of a Dropdown date picker
- Creation of variables for current date and others in the past or future
- choosing date from dropdowns inside the date picker

"""

from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_dropdown_date_picker(driver):
    url = "https://demo.automationtesting.in/Datepicker.html"
    driver.get(url)

    driver.find_element(By.ID, "datepicker2").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".datepick-popup")))

    current_date = datetime.now()
    print(current_date)

    next_day = current_date + timedelta(days=1)
    print(next_day)
    # Next day shows me exactly 24 hours after. But what if I just want the next day, not exactly 24 hours? examples of things
    only_next_day = (str(next_day.day))
    print(only_next_day)

    current_month = datetime.now().month
    print(current_month)
    current_year = current_date.year
    print(current_year)
    next_month = (current_month % 12) + 1
    print(next_month)

    # Click on the month dropdown and select next month, year and day
    next_month_year = f"{next_month}/{current_year}"  # This is because this particular dropdown shows the month and the year in the code. Not sure if this will come up often in other date pickers

    month_dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
    select = Select(month_dropdown)
    select.select_by_value(str(next_month_year))
    year_dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the year']")
    select = Select(year_dropdown)
    select.select_by_visible_text("2024")
    driver.find_element(By.LINK_TEXT, only_next_day).click()
