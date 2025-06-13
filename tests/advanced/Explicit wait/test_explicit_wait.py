from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_explicit_wait(driver):

    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    #Creating a variable for the element and giving it up to 10 secs to be located, then clicking it
    logout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='logout_sidebar_link']")))
    logout.click()