import time

#using the csv library
import csv
from selenium.webdriver.common.by import By


def test_data_driven_py(driver):
    # adding a path for the csv file
    csv_file = 'advanced/Data Driven Testing/test_data.csv'

    # Creating an empty list for the data
    test_data = []

    # opening the file in read mode and adding the info to my empty list
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_data.append(row)
    print(test_data)

    # using that now not empty list for testing
    for data in test_data:
        driver.get('https://www.saucedemo.com/')
        time.sleep(3)
        driver.find_element(By.ID, 'user-name').send_keys(data['username'])
        driver.find_element(By.ID, 'password').send_keys(data['password '])
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
        time.sleep(2)
        driver.find_element(By.ID, 'logout_sidebar_link').click()
        time.sleep(3)

