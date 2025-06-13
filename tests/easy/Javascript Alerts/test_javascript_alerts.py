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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


def test_javascript_alerts(driver):

    url = "https://the-internet.herokuapp.com/javascript_alerts"

    driver.get(url)

    wait = WebDriverWait(driver, 10)  # ✅ Initialize explicit wait

    # Triggering the alert
    js_alert = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
    js_alert.click()

    # Switching to the alert
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)

    # Accepting alert
    alert.accept()

    # Clicking alert that comes with confirmation
    js_confirm =wait.until((EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsConfirm()']"))))
    js_confirm.click()

    # Switching to alert
    wait.until(EC.alert_is_present())
    confirm = driver.switch_to.alert

    # Checking the text to ensure I switched correctly
    print(confirm.text)

    # Dismiss alert (Pressing cancel)
    confirm.dismiss()

    # Now the prompt! On this one, I enter a text to close the alert
    js_prompt = wait.until((EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsPrompt()']"))))
    js_prompt.click()

    # Switch to alert and checking the content
    wait.until(EC.alert_is_present())
    prompt = driver.switch_to.alert
    print(prompt.text)

    # Sending keys and accepting
    alert.send_keys("Demián")
    alert.accept()


