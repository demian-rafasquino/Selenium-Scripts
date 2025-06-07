"""
Test Case: Javascript alerts

This script tests the handling of Javascript alerts

1. Opens the browser and navigates to a website with three different Javascript alerts
2. Click the first one(regular alert) and accept it
3. Clicks the second one (confirmation alert) and dismisses it.
4. Clicks the third one (prompt) and enters information before confirming



This test demonstrates:
- Handling of different types of Javascript alerts
- Triggering alerts, accepting, dismissing and entering information

"""



from selenium.webdriver.common.by import By
import time

def test_javascript_alerts(driver):
    url = "https://the-internet.herokuapp.com/javascript_alerts"

    driver.get(url)

    # Triggering the alert
    js_alert = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
    js_alert.click()

    # Switching to the alert
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    time.sleep(3)

    # Accepting alert
    alert.accept()
    time.sleep(2)

    # Clicking alert that comes with confirmation
    js_confirm = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
    js_confirm.click()

    # Switching to alert
    confirm = driver.switch_to.alert

    # Checking the text to ensure I switched correctly
    confirm_text = confirm.text
    print(confirm_text)
    time.sleep(2)

    # Dismiss alert (Pressing cancel)
    confirm.dismiss()
    time.sleep(2)

    # Now the prompt! On this one, I enter a text to close the alert
    js_prompt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
    js_prompt.click()
    time.sleep(2)

    # Switch to alert and checking the content
    prompt = driver.switch_to.alert
    prompt_text = prompt.text
    print(prompt_text)

    # Sending keys and accepting
    alert.send_keys("Demián")
    time.sleep(2)
    alert.accept()
    time.sleep(2)

