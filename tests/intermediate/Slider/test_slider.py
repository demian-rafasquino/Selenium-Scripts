"""
Test Case: Slider

This script tests how to handle using a slider through Selenium

1. Opens the browser and navigates to a website with a slider
2. Grabs the slider by clicking and holding
3. Drags the slider to a specified input
4. Repeats


This test demonstrates:
- Click and hold actions
- Drag action by offset


"""


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slider(driver):
    driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    # Finding slider
    slider = driver.find_element(By.XPATH, "//input[@type='range']")
    value_display = driver.find_element(By.ID, "range")
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)


    # Action chain to click and hold, then slide by offset
    actions.click_and_hold(slider).move_by_offset(50, 0).release().perform()
    wait.until(lambda d: value_display.text != "0")
    assert value_display.text != "0"
    print(value_display.text)

    actions.click_and_hold(slider).move_by_offset(25, 0).release().perform()
    wait.until(lambda d: float(value_display.text) > 0.5)
    assert value_display.text > "0.5"
    print(value_display.text)

    # If the offset is more than the slider has, it just goes to the top
    actions.click_and_hold(slider).move_by_offset(500, 0).release().perform()
    wait.until(lambda d: value_display.text == "5")  # 5 is the max value
    assert value_display.text == "5"
    print(value_display.text)
