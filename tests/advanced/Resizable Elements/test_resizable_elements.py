from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_resizable_elements(driver):
    wait = WebDriverWait(driver, 10)
    url = "https://demo.automationtesting.in/Resizable.html"
    driver.get(url)
    resize = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//div[contains(@class, 'ui-resizable-handle') and contains(@class, 'ui-resizable-se')]"
    )))

    # Finding the current size of the element
    initial_resizable_element = wait.until(EC.presence_of_element_located((By.ID, "resizable")))
    initial_size = initial_resizable_element.size
    print("Initial size: ", initial_size)

    action_chains = ActionChains(driver)
    action_chains.click_and_hold(resize).move_by_offset(100, 100).release().perform()
    wait.until(lambda d: d.find_element(By.ID, "resizable").size != initial_size)

    # Now to check the new size
    resized_element = initial_resizable_element.size
    print("Resized Element: ", resized_element)

