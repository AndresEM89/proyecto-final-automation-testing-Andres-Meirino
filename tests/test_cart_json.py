from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.data_reader import read_products_json
from utils.logger import logger  # <-- Importamos tu logger

def test_cart_json(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)
    
    logger.info("JSON: Leyendo lista de productos desde el archivo de datos")
    productos = read_products_json()

    for producto in productos:
        logger.info(f"JSON: Agregando producto '{producto['nombre']}' al carrito")
        inventory_page.agregar_producto_por_nombre(producto["nombre"])

    logger.info("JSON: Navegando hacia la página del carrito")
    inventory_page.ir_al_carrito()

    productos_carrito = cart_page.obtener_productos_carrito()

    logger.info("JSON: Validando coincidencia de productos esperados vs carrito")
    for producto_esperado in productos:
        encontrado = False
        for producto_carrito in productos_carrito:
            if (producto_carrito["nombre"] == producto_esperado["nombre"] and producto_carrito["precio"] == producto_esperado["precio"]):
                encontrado = True
                break

        assert encontrado, f"producto incorrecto o faltante: {producto_esperado['nombre']}"        
    logger.info("JSON: Todos los productos del JSON se validaron correctamente en el carro")