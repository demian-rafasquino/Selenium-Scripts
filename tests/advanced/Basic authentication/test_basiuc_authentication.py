import time


def test_basic_authentication(driver):
    username = "admin"
    password = "admin"
    # Since I can't inspect the html for the authenticator, I can just append the username and password to the url like this
    # https://username:password@domain/path

    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    time.sleep(2)
