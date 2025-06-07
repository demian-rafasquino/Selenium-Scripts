"""
Test Case: Dropdowns

This script tests the handling of dropdowns

1. Opens the browser and navigates to a website
2. Finds a specific dropdown
3. Explore ways to select a select HTML dropdown element (text, index, value)
4. Checks how many options the dropdown has
5. Chooses an option if it is there.


This test demonstrates:
- Finding and Switching to Iframe
- Navigating through a nested iframe
- Switching back to broader webpage

"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_dropdown(driver):
    dropdown_page = 'https://the-internet.herokuapp.com/dropdown'
    driver.get(dropdown_page)
    driver.maximize_window()
    dropdown_element = driver.find_element(By.ID, 'dropdown')
    select = Select(dropdown_element)

    # We can select the value by visible text, index or using a value
    # By visible text
    # select.select_by_visible_text('Option 2')
    # #By index
    # select.select_by_index(1)
    # #By Value
    # select.select_by_value("2")
    # #THESE METHODS ARE FOR WHEN THE DROPDOWN IS A SELECT HTML ELEMENT. IF IT'S NOT, JUST USING .CLICK() WILL DO

    # ----------------------

    # NOW, TO CHECK ON HOW MANY OPTIONS ARE IN THE DROPDOWN, DO THIS:
    option_count = len(select.options)
    expected_count = 3
    if option_count == expected_count:
        print('All good')
    else:
        print("incorrect dropdown option count")

    # How to tell it to select an option if it's there:
    target_value = "Option 2"
    select = Select(dropdown_element)
    for option in select.options:
        if option.text == target_value:
            option.click()
            print(f"Selected Option is {target_value}")
            break
        else:
            print(f"Option '{target_value}' not found")

