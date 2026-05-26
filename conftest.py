import pytest
from selenium import webdriver
#from utils.login_page import login

@pytest.fixture
def driver():
    options=webdriver.FirefoxOptions()
    options.add_argument("--incognito")

    driver=webdriver.Firefox(options=options)
    yield driver
    driver.quit()

#@pytest.fixture
#def login_in_driver(driver):
#    login(driver)
#    return driver