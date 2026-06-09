import requests

headers ={
"x-api-key":"pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d" 
}
def test_login_valido():
    body={
       "email": "eve.holt@reqres.in", 
       "password": "cityslicka"
    }
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    assert response.status_code==200

def test_login_sin_password():
    body={
       "email": "eve.holt@reqres.in", 
       
    }
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    assert response.status_code==400

def test_create_user():
    body={
       "name": "jose", "email": "jose@gmail.com", "password": "123456"
    }
    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)
    data=response.json()
    print(data)

    assert response.status_code==201    
    assert data["name"]==body["name"]
    assert data["email"]==body["email"]

def test_delete_user():
    respose=requests.delete("https://reqres.in/api/users/2", headers=headers)
    assert respose.status_code==204

def test_get_user():
    response = requests.get("https://reqres.in/api/users", headers=headers)

    assert response.status_code==200
    assert response.elapsed.total_seconds()<2, f"Tiempo de respuesta elevado: {response.elapsed.total_seconds()}"
    #print("tiempo de respuesta", response.elapsed.total_seconds())