README - Proyecto de Automatización QA 
1. Propósito del Proyecto
El objetivo de esta pre-entrega es aplicar conocimientos de Selenium WebDriver y Python para automatizar flujos básicos en la web saucedemo.com.

2. Tecnologías Requeridas
- Python
- Pytest (estructura de testing)
- Selenium WebDriver (automatización)
- Git y GitHub (control de versiones)

3. Estructura del Proyecto
- tests/: Archivos de prueba (ej. test_saucedemo.py).
- utils/: Funciones auxiliares y configuración del driver.
- reports/: Reportes HTML generados.
- datos/: Datos externos (si aplica).

4. Instrucciones de Instalación
   1. copiar URL de repositorio
      https://github.com/AndresEM89/pre-entrega-automation-testing-Andres-Meirino.git
   2. Abrir la terminal y Ubicate en la carpeta de tu computadora donde quieras que se guarde el proyecto.
      cd Desktop/Proyectos
   3.  Ejecutar el comando de clonación
   git clone https://github.com/AndresEM89/pre-entrega-automation-testing-Andres-Meirino.git
   4. Una vez que termine la descarga, se habrá creado una carpeta nueva con el nombre del repositorio.

5. Cómo ejecutar las pruebas
Para correr los tests y generar el reporte HTML, usa en consola el comando:
python -m pytest

6. Casos de Prueba Incluidos
- Automatización de Login (credenciales válidas).
- Navegación y Verificación del Catálogo (título y productos).
- Interacción con Carrito (añadir producto y verificar contador).