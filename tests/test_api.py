import requests
from utils.logger import logger  # <-- Importamos tu logger

headers = {
    "x-api-key": "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d"
}

def test_login_valido():
    body = {
       "email": "eve.holt@reqres.in", 
       "password": "cityslicka"
    }
    logger.info("API: Intentando login válido en ReqRes")
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    
    logger.info(f"API: Respuesta recibida con status {response.status_code}")
    assert response.status_code == 200

def test_login_sin_password():
    body = {
       "email": "eve.holt@reqres.in", 
    }
    logger.warning("API: Intentando login sin contraseña (flujo negativo)")
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    
    logger.info(f"API: Respuesta recibida con status {response.status_code}")
    assert response.status_code == 400

def test_create_user():
    body = {
       "name": "jose", "email": "jose@gmail.com", "password": "123456"
    }
    logger.info(f"API: Intentando crear usuario: {body['name']}")
    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)
    data = response.json()
    print(data)

    logger.info(f"API: Validando creación de usuario con status {response.status_code}")
    assert response.status_code == 201    
    assert data["name"] == body["name"]
    assert data["email"] == body["email"]

def test_delete_user():
    logger.info("API: Intentando eliminar usuario con ID 2")
    respose = requests.delete("https://reqres.in/api/users/2", headers=headers)
    
    logger.info(f"API: Validando eliminación con status {respose.status_code}")
    assert respose.status_code == 204

def test_get_user():
    logger.info("API: Solicitando lista de usuarios")
    response = requests.get("https://reqres.in/api/users", headers=headers)

    tiempo_respuesta = response.elapsed.total_seconds()
    
    try:
        assert response.status_code == 200
        assert tiempo_respuesta < 2
        logger.info(f"API: Petición GET exitosa en {tiempo_respuesta} segundos")
    except AssertionError as e:
        if tiempo_respuesta >= 2:
            # CAMBIO AQUÍ: Si el servidor tarda demasiado, es una alerta CRÍTICA
            logger.critical(f"PERFORMANCE CRÍTICA: El servidor demoró {tiempo_respuesta}s en responder. Posible caída o degradación.")
        else:
            logger.error(f"API: Falló la petición GET con status {response.status_code}")
        raise e