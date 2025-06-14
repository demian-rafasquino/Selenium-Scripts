"""
Test Case: Mouse hover

This script tests how to hover the mouse to show non visible options on the site with Selenium

1. Opens the browser and navigates to a website
2. Hovers the mouth other an option to show the hidden options
3. Clicks on one of the hidden options once they become visible through the hover action


This test demonstrates:
- Hover action over web elements to show non visible options
- Clicking on said non visible options once they become visible


"""

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_mouse_hover(driver):
    url = "https://demo.automationtesting.in/Datepicker.html"
    driver.get(url)

    # Can't click on the element that only appears when hovering the mouse over a place.
    # If I try, it gives an error because the element is present but not interactable
    # Using action chains. They can automate low level interactions like mouse movement, mouse buttons, key press and context menu interactions

    actions = ActionChains(driver)
    hover_element = driver.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
    actions.move_to_element(hover_element).perform()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='Frames.html")))
    driver.find_element(By.CSS_SELECTOR, "a[href='Frames.html']").click()


