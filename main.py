# Paolo Lanaro
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = 'https://azenta.wd1.myworkdayjobs.com/Azenta_External_Site/login?redirect=%2FAzenta_External_Site%2Fjob%2FBillerica%2FHardware-Engineering-Co-Op---May-Dec_R20240891-1%2Fapply'

def basic_example(URL, title):
    # Create the webdriver on Firefox
    driver = webdriver.Firefox()
    # Navigate to the URL specified
    driver.get(URL)
    # Assert some title string is in the driver's title
    assert title in driver.title

def running_example(URL, title):
    driver = webdriver.Firefox()
    driver.get(URL)
    assert title in driver.title

    # Get elements, make a list of useful elements, navigate to elements that are useful click buttons
    breakpoint()

    time.sleep(5)
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
    # basic_example('https://duckduckgo.com', 'Duck')
    running_example(URL, 'Workday')



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
