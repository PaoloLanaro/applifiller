# Paolo Lanaro
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Login URL:
# URL = 'https://azenta.wd1.myworkdayjobs.com/Azenta_External_Site/login?redirect=%2FAzenta_External_Site%2Fjob%2FBillerica%2FHardware-Engineering-Co-Op---May-Dec_R20240891-1%2Fapply'
# Application URL:
URL = 'https://jobs.lever.co/analyticpartners/ee9ec916-0a8c-4550-b80d-afdcf702ed4b'
user_json = 'user.json'

def check_user_loaded_data():
    if not os.path.exists(user_json):
        return False

    with open(user_json, 'r') as f:
        global data
        data = json.load(f)

    # Rough version of 'make sure we have data'
    assert data['email']
    assert data['first_name']
    assert data['last_name']
    assert data['phone']
    assert data['birthdate']
    assert data['address']
    assert data['path_to_resume']

def basic_example(URL, title):
    # Create the webdriver on Firefox
    driver = webdriver.Firefox()
    # Navigate to the URL specified
    driver.get(URL)
    # Assert some title string is in the driver's title
    assert title in driver.title

def find_attribute(element, search_tag, expected_tag, case_sensitive = False):
    try:
        value = element.get_attribute(search_tag)
        if (case_sensitive and value == expected_tag) or (not case_sensitive and value.lower() == expected_tag.lower()):
            return True

    except:
        pass

    return False

def find_attributes(element, attributes, expected_tag):
    return any([find_attribute(element, attribute, expected_tag) for attribute in attributes])

def running_example(URL, title):
    driver = webdriver.Firefox()
    driver.get(URL)
    assert title in driver.title
    time.sleep(2)

    class_names = ['postings-btn-wrapper']
    css_tags = ['input', 'button']
    # for tag in tags
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input')
    for input in inputs:

        if find_attributes(input, ['data-automation-id', 'autocomplete'], 'email'):
            # we have an email form!
            print('email form detected')
            input.send_keys(data['email'])
            breakpoint()
        # if find_attributes(input, []

    # Get elements, make a list of useful elements, navigate to elements that are useful click buttons
    breakpoint()

    elements = driver.find_elements()
    print(elements)

    # Find the "search bar"
    elem = driver.find_element(By.NAME, "q")
    # Clear any existing searches
    elem.clear()
    # Send input to element
    elem.send_keys("www.paololanaro.dev")
    elem.send_keys(Keys.RETURN)

if __name__ == '__main__':
    # Check whether we have data for user information
    check_user_loaded_data()
    # basic_example('https://duckduckgo.com', 'Duck')
    title = 'Workday'
    title = 'Analytic'
    running_example(URL, title)



# (Pdb) inputs = driver.find_elements(By.CSS_SELECTOR, 'input')
### [<selenium.webdriver.remote.webelement.WebElement (session="a8be0272-8ae1-4962-8cd9-acf01f594854", element="cb5a6840-5f03-48d9-9e34-801275337283")>, <selenium.webdriver.remote.webelement.WebElement (session="a8be0272-8ae1-4962-8cd9-acf01f594854", element="d3553dff-9d82-4d46-a887-5ff4e68a960b")>, <selenium.webdriver.remote.webelement.WebElement (session="a8be0272-8ae1-4962-8cd9-acf01f594854", element="45e861fa-c041-4b48-943e-8246b5d3b0ec")>]
# (Pdb) f_in = inputs[0]
# (Pdb) f_in
# (Pdb) f_in.click()
# *** selenium.common.exceptions.ElementClickInterceptedException: Message: Element <input id="input-4" class="css-17hphhs" type="text"> is not clickable at point (960,54) because another element <div class="css-1b2fe75"> obscures it
# (Pdb) f_in.get_attribute('id')
# 'input-4'
# (Pdb) f_in.get_attribute('data-automation-id')
# 'email'
# (Pdb) f_in.get_attribute('data-automation-id')
# 'email'
# (Pdb) f_in.get_attribute('autocomplete')
# 'email'
# (Pdb) f_in.get_attribute('type')
# 'text'
# (Pdb) q



# WATCH OUT FOR!!!
# <div>
    # <div class="css-79elbk">
    # <label for="c445e1fe-bbd6-4668-84c5-65ffac0e3426" class="css-i19yjz">Enter website. This input is for robots only, do not enter if you're human.</label>
        # <input data-automation-id="beecatcher" id="c445e1fe-bbd6-4668-84c5-65ffac0e3426" name="website" type="text" class="css-umjazw">
    # </div>
# </div>
