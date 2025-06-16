#using the csv library
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_data_driven_py(driver):
    # adding a path for the csv file
    csv_file = 'advanced/Data Driven Testing/test_data.csv'

    # Creating an empty list for the data
    test_data = []

    # opening the file in read mode and adding the info to my empty list
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cleaned_row = {key.strip(): value.strip() for key, value in row.items()}
            test_data.append(cleaned_row)

    # using that now not empty list for testing
    for data in test_data:
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

