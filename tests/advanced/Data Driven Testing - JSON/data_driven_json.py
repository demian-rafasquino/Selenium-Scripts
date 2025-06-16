
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#importing json
import json



def test_data_driven_json(driver):
    # Opening the file
    with open('advanced/Data Driven Testing/testing_data.json', 'r') as file:
        test_data = json.load(file)

    for data in test_data['users']:  # letting pycharm know that the info is inside "users" section of the json
        if not data.get("username") or not data.get("password"):
            continue
        wait = WebDriverWait(driver, 10)
        driver.get('https://www.saucedemo.com/')
        wait.until(EC.presence_of_element_located((By.ID, 'user-name')))

        driver.find_element(By.ID, 'user-name').send_keys(data['username'])
        driver.find_element(By.ID, 'password').send_keys(data['password'])
        driver.find_element(By.ID, 'login-button').click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

        driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
        wait.until(EC.presence_of_element_located((By.ID, 'logout_sidebar_link')))

        driver.find_element(By.ID, 'logout_sidebar_link').click()
        assert driver.current_url == 'https://www.saucedemo.com/'


