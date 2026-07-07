from selenium.webdriver.common.by import By 
from utils.logger import logger

class LoginPage:
    def __init__(self, driver):
        
        self.driver=driver

        #selectores
        self.username_input=(By.ID, "user-name")
        self.password_input=(By.ID, "password")
        self.login_button=(By.ID, "login-button")
        self.error_password = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        try:
            self.driver.get("https://www.saucedemo.com/")
        except:
            logger.critical("No se pudo conectar.")

    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario) 

    def ingresar_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()    

    def login(self, usuario, password):
        self.open()    
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_login()

    def get_error_message(self):
        error = self.driver.find_element(*self.error_password).text
        print(error)
        return error

        
