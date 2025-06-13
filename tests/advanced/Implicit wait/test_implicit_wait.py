from selenium.webdriver.common.by import By

def test_implicit_wait(driver):
    driver.implicitly_wait(2)  # meaning it waits up to 10 seconds for the interactable elements to load before sending an error
    driver.get('https://www.saucedemo.com/')

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()

    driver.find_element(By.ID, 'logout_sidebar_link').click()


