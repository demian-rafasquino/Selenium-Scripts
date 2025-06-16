from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_basic_authentication(driver):
    username = "admin"
    password = "admin"
    # Since I can't inspect the html for the authenticator, I can just append the username and password to the url like this
    # https://username:password@domain/path

    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    logged_in = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='example'] p")))
    assert logged_in.text == "Congratulations! You must have the proper credentials."
