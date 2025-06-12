import time
from selenium.webdriver.common.by import By

#importing json
import json



def test_data_driven_json(driver):
    # Opening the file
    with open('advanced/Data Driven Testing/testing_data.json', 'r') as file:
        test_data = json.load(file)

    for data in test_data['users']:  # letting pycharm know that the info is inside "users" section of the json
        driver.get('https://www.saucedemo.com/')
        time.sleep(3)
        driver.find_element(By.ID, 'user-name').send_keys(data['username'])
        driver.find_element(By.ID, 'password').send_keys(data['password'])
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
        time.sleep(2)
        driver.find_element(By.ID, 'logout_sidebar_link').click()
        time.sleep(3)


