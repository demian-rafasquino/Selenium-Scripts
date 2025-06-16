"""
Test Case: nested iframes

This script tests the handling of nested iframes

1. Opens the browser and navigates to a website
2. Finds a specific iframe.
3. Switches to iframe
4. Switches to an iframe inside it
5. Checks the content to ensure it's the correct one
6. Switches back to default content.
7. Switches to another iframe
8. Checks content

This test demonstrates:
- Finding and Switching to Iframe
- Navigating through a nested iframe
- Switching back to broader webpage

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#EXPLANATION
#Nested frames are frames inside of frames.
# In this example, there's a frameset with 2 frames. And then, inside the top one, there's 3 and the bottom one is only one
#I will go to the one in the middle of the big frame up top, and then to the big one on the bottom

def test_nested_frames(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    # Switching to top frame
    driver.switch_to.frame("frame-top")

    # Now switch to the middle frame inside the top frame
    driver.switch_to.frame("frame-middle")

    # Checking its content
    content_of_frame = wait.until(
        EC.presence_of_element_located((By.ID, "content"))
    ).text
    print("Content in middle frame: ", content_of_frame)

    # Now I need to come out of this frame inside the top frame, to go to the bottom frame
    # First switch to default content
    driver.switch_to.default_content()

    # Now to the bottom frame.
    driver.switch_to.frame("frame-bottom")

    # Checking the content
    content_of_bottom = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    ).text
    print("Content in bottom frame: ", content_of_bottom)
