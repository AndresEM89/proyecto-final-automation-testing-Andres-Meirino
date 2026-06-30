from pages.login_page import LoginPage
from utils.data_reader import read_user_csv
import pytest
from utils.logger import logger  # <-- Importamos tu logger

@pytest.mark.parametrize("user", read_user_csv())
def test_login(driver, user):
    login_page = LoginPage(driver)

    logger.info(f"CSV Login: Probando credenciales de usuario: '{user['username']}' (Válido: {user['valid']})")
    login_page.login(user["username"], user["password"])
    
    if user["valid"] == "true":
        logger.info("CSV Login: Validando redirección exitosa a la página de inventario")
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        logger.info("CSV Login: Validando presencia de mensaje de error 'Epic sadface'")
        error = login_page.get_error_message()
        assert "Epic sadface" in error