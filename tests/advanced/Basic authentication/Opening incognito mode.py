import time
from selenium.webdriver.firefox.options import  Options

def test_incognito_firefox(driver)
    firefox_options = Options()
    firefox_options.add_argument("--private")

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    time.sleep((2))
    driver.get("https://the-internet.herokuapp.com/")
