"""
Test Case: Viewport practice

This script tests the usage of different viewports to check a website

1. Opens the browser and navigates to the set page
2. changes the resolution of the website 4 times.


This test demonstrates:
- Changing viewport sizes with Selenium

"""


import time

def test_viewports(driver):
    viewports = [(1024, 768), (768, 1024), (375, 667), (414, 896)]
    driver.get('https://www.google.com')

    # Using try so it doesn't crash if one of these fails
    try:
        for width, height in viewports:
            driver.set_window_size(width, height)
            time.sleep(2)
    finally:
        driver.close()



