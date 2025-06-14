"""
Test Case: iframes handling

This script tests the handling of iframes

1. Opens the browser and navigates to a website
2. Finds a specific iframe.
3. Switches to iframe
4. Performs an action inside the iframe
5. Switches back to default content
6. Performs an action on the default content(outside of iframe)

This test demonstrates:
- Finding and Switching to Iframe
- Performance of a specific task inside iframe
- Switching back to broader webpage

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_iframe(driver):
    driver.get("https://www.automationtesting.co.uk/iframes.html")
    second_iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src='https://www.youtube.com/embed/jNQXAC9IVRw']")))


    driver.switch_to.frame(second_iframe)
    video_player = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "movie_player")))
    video_player.click()


