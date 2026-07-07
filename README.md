README - Proyecto de Automatización QA 

1. Propósito del Proyecto
El objetivo de este proyecto es implementar un framework de automatización robusto utilizando Python para validar de manera integral tanto la interfaz de usuario (UI) de Sauce Demo (https://www.saucedemo.com/) como los endpoints de la API de pruebas ReqRes (https://reqres.in/). El framework cuenta con una arquitectura escalable basada en Page Object Model (POM), manejo avanzado de datos externos, reportabilidad y un sistema detallado de trazabilidad mediante logging.

2. Tecnologías Utilizadas
- Python (Lenguaje de programación base)
- Selenium WebDriver (Automatización de pruebas UI)
- Requests (Validación y consumo de servicios API)
- Pytest (Estructura de testing, parametrización y aserciones)
- Git y GitHub (Control de versiones)

3. Estructura del Proyecto
Proyecto/
│
├── pages/             # Clases bajo el patrón Page Object Model (POM)
├── tests/             # Suite de pruebas automatizadas (UI y API)
├── utils/             # Funciones auxiliares, lectura de datos y configuración del Logger
├── data/              # Archivos de datos externos (CSV, JSON) para pruebas guiadas por datos
├── reportes/          # Reportes gráficos generados en formato HTML
└── logs/              # Archivos históricos de trazas (.log) generados dinámicamente

4. Instrucciones de Instalación y Configuración

1. Clonar el repositorio:
   Abre una terminal, ubícate en la carpeta donde deseas guardar el proyecto y ejecuta:
   git clone https://github.com/AndresEM89/proyecto-final-automation-testing-Andres-Meirino.git

2. Acceder al directorio:
   cd proyecto-final-automation-testing-Andres-Meirino

3. Instalar dependencias:
   Asegúrate de contar con las librerías necesarias ejecutando:
   pip install selenium requests pytest pytest-html

5. Sistema de Logging y Reportabilidad
El framework implementa un Logger unificado personalizado que registra la ejecución en tiempo real tanto en la consola como en archivos de texto persistentes dentro del directorio de logs. Cumpliendo con estándares profesionales de depuración, se utilizan múltiples niveles de severidad:
- INFO: Seguimiento del flujo normal de los tests.
- WARNING: Alertas controladas en flujos negativos o respuestas esperadas de error.
- ERROR: Captura de fallos en aserciones o excepciones de la UI sin detener la suite de manera abrupta.
- CRITICAL: Errores graves de infraestructura o degradación crítica en tiempos de respuesta de servidores.

6. Cómo ejecutar las pruebas
Para ejecutar toda la suite de pruebas (UI y API) de manera consecutiva y generar de forma automática el reporte gráfico en HTML, ejecuta en tu consola:
python -m pytest -v

Si deseas ejecutar únicamente las pruebas de integración de servicios Web (API):
python -m pytest -v tests/test_api.py -s

7. Casos de Prueba Incluidos

* Pruebas de Interfaz de Usuario (UI):
- Autenticación (Login): Validación de accesos con usuarios válidos y control de mensajes de error frente a contraseñas inválidas.
- Pruebas Guiadas por Datos (DDT): Inicio de sesión iterativo parametrizado mediante la lectura de un archivo estructurado en formato CSV.
- Navigation e Inventario: Verificación de títulos, carga de elementos dinámicos en la interfaz y visibilidad de componentes base.
- Flujo de Carrito de Compras: Interacción con el catálogo de productos, validación incremental del contador de artículos y persistencia de datos guiada por un archivo JSON.

* Pruebas de Servicios Web (API REST):
- Autenticación válida e inválida (flujo negativo con control de estados HTTP).
- Creación de registros de usuario y aserción de la integridad de los datos devueltos en formato JSON.
- Eliminación de registros con validación de códigos de estado específicos (204 No Content).
- Pruebas de rendimiento sobre el tiempo de respuesta del servidor (alertas automáticas frente a latencias mayores a 2 segundos).