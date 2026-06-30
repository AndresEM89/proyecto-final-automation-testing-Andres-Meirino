import pathlib
import pytest
import pytest_html
from selenium import webdriver
from pages.login_page import LoginPage
from utils.data_reader import read_user_csv


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--incognito")

    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)
    user = read_user_csv()[0]

    login_page.login(user["username"], user["password"])
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report = outcome.get_result()

    # Se ejecuta solo si el test falla durante la llamada del test ('call')
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            target = pathlib.Path("reportes/screenshots")
            target.mkdir(parents=True, exist_ok=True)

            file_name = target / f"{item.name}.png"
            driver.save_screenshot(str(file_name))

            # 🚀 SOLUCIÓN COMPATIBLE CON V4:
            # Usamos el constructor oficial de la librería. Esto le inyecta 
            # internamente la clave 'extension' y evita el colapso del plugin.
            extras = getattr(report, "extras", [])
            extras.append(
                pytest_html.extras.image(
                    f"screenshots/{item.name}.png", 
                    name="screenshot"
                )
            )
            report.extras = extras