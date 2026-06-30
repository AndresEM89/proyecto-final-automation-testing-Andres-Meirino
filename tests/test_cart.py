from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.logger import logger  # <-- Importamos tu logger

def test_cart(driver_logged):
    driver = driver_logged
    
    logger.info("Carrito: Agregando el primer producto disponible al carro")
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    
    logger.info("Carrito: Validando que el contador del badge aumente a 1")
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge") 
    assert contador_cart.text == "1", "Fallo en contador del carro"

    first_product = driver.find_elements(By.CLASS_NAME, "inventory_item_name ")[0].text 
    
    logger.info(f"Carrito: Entrando al carrito para verificar el producto: '{first_product}'")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_product = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    assert first_product == cart_product, "El producto agregado no coincide"
    logger.info("Carrito: Verificación de producto en carrito exitosa")