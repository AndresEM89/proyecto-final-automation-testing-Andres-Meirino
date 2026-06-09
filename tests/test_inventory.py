from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_inventory_title(driver_logged):
  inventory_page=InventoryPage(driver_logged)
   
  titulo =inventory_page.obtener_titulo()
  assert titulo=="Swag Labs", "El titulo de la pagina no es el correcto"

def test_productos_visibles(driver_logged):
  inventory_page=InventoryPage(driver_logged)
  
  productos=inventory_page.obtener_productos()
  assert   len(productos)>0


def test_ui_elements(driver_logged):
  inventory_page=InventoryPage(driver_logged)
  
  assert inventory_page.menu_visible(), "El menu no esta presente en la pagina"
  assert inventory_page.filtro_visible(), "El filtro no esta presente"
