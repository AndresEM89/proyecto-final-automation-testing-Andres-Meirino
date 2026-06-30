from pages.login_page import LoginPage
from utils.logger import logger


def test_login_valid(driver):
    logger.info("Inicializando driver para test_login_ok")
    login_page=LoginPage(driver)
    logger.info("Ingresando datos para la prueba")
    login_page.login("standard_user", "secret_sauce")
    logger.info("Intentando iniciar sesión con usuario válido...")
    assert "/inventory.html" in driver.current_url, "no se redirigio al inventario"
    logger.info("sesion iniciada correctamente")

def test_login_invalid_password(driver):
    logger.info("Inicializando la página de Login para contraseña inválida")
    login_page = LoginPage(driver)
    
    logger.info("Ingresando datos con contraseña incorrecta")
    login_page.login("standard_user", "23456")
    
    logger.info("Capturando el mensaje de error")
    error = login_page.get_error_message()
    
    #assert "Mensaje de ERROR 371"
    assert error == "Epic sadface: Username and password do not match any user in this service"
    
    logger.info("Validación del error completada")