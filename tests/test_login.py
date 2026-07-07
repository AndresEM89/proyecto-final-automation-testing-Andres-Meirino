from pages.login_page import LoginPage
from utils.logger import logger


def test_login_valid(driver):
    logger.info("Inicializando driver para test_login_ok")
    login_page=LoginPage(driver)
    logger.info("Ingresando datos para la prueba")
    login_page.login("standard_user", "secret_sauce")
    logger.info("Intentando iniciar sesión con usuario válido...")
    if "/inventory.html" not in driver.current_url:
        logger.error(f"No se pudo ingresar correctamente, el URL actual:{driver.current_url}")   
    assert "/inventory.html" in driver.current_url, "no se redirigio al inventario"
    logger.info("sesion iniciada correctamente")

def test_login_invalid_password(driver):
    logger.info("Inicializando la página de Login para contraseña inválida")
    login_page = LoginPage(driver)
    
    logger.info("Ingresando datos con contraseña incorrecta")
    login_page.login("standard_user", "23456")
    
    logger.info("Capturando el mensaje de error")
    error = login_page.get_error_message()
    
    try:
        assert error == "Epic sadface: Username and password do not match any user in this service"
        logger.info("Validación del error completada")
    except AssertionError as e:
        # CAMBIO AQUÍ: Capturamos el fallo de la aserción y lo registramos como ERROR
        logger.error(f"Fallo en validación de credenciales inválidas. Se esperaba el mensaje clásico pero se obtuvo: '{error}'")
        raise e