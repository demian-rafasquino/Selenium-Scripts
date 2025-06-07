"""
Test Case: Broken links

This script tests all links on a website and returns the broken ones with status over 400

1. Opens the browser and navigates to the website
2. Finds all links on the website.
3. Reports total amount of links
4. Checks href response status code of all links
5. Reports all links with a response status code over 400

This test demonstrates:
- Broken links handling with Selenium

"""



from selenium.webdriver.common.by import By
import requests

def test_broken_links(driver):
    url = "https://jqueryui.com/"
    driver.get(url)

    # Get all links from the page
    all_links = driver.find_elements(By.TAG_NAME, "a")  # "a" is found in the html code
    print(f"Total number of links in the page is: {len(all_links)}")

    # Loop through all available links one by one and get the href, check the response and print the broken ones
    for link in all_links:
        href = link.get_attribute('href')
        response = requests.get(href)
        if response.status_code >= 400:
            print(f"Broken Link: {href}(status code {response.status_code})")
