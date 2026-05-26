#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

from pages.login_page import LoginPage

def test_login_valid(driver):
    login_page=LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "/inventory.html" in driver.current_url, "no se redirigio al inventario"

def test_login_invalid_password(driver):
    login_page=LoginPage(driver)
    login_page.login("standard_user", "23456")
    error=login_page.get_error_password_mensage()
    assert "Mensaje de ERROR 371"
