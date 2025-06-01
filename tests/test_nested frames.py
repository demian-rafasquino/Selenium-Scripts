from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Nested frames are frames inside of frames.
# In this example, there's a frameset with 2 frames. And then, inside the top one, there's 3 and the bottom one is only one
#In this example, we will go to the one in the middle of the big frame up top, and then to the big one on the bottom
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/nested_frames")

#Switching to top frame
browser.switch_to.frame("frame-top")

#Now switch to the middle frame
browser.switch_to.frame("frame-middle")

content_of_frame = browser.find_element(By.ID, "content").text
print("Content in middle frame: ", content_of_frame)

#Now I need to come out of this frame inside the top frame, to go to the bottom frame
#First switch to default content

browser.switch_to.default_content()

#Now to the bottom frame.
browser.switch_to.frame("frame-bottom")

content_of_bottom = browser.find_element(By.TAG_NAME, "body").text

print("Content in bottom frame: ", content_of_bottom)
time.sleep(3)
browser.quit()
