import requests

# Hacemos la solicitud HTTP
resp = requests.get('https://api.github.com/')

# Imprimimos el código de estado 
print(resp.status_code) # 200 = OK

# Vemos el tipo de contenido devuelto
print(resp.headers['content-type']) # application/json

# Convertimos el JSON a dict de Python
payload = resp.json()
print(payload['current_user_url'])

#GET
URL = 'https://reqres.in/api/users?page=2'
def test_get_users():
 r = requests.get(URL)
 assert r.status_code == 200
 data = r.json()
 assert data['page'] == 2
 assert len(data['data']) > 0 # al menos un usuario

 #POST
CREATE_URL = 'https://reqres.in/api/users'
def test_create_user():
 payload = {'name': 'Matias QA', 'job': 'tester'}
 r = requests.post(CREATE_URL, json=payload)
 assert r.status_code == 201 # Created
 new_user = r.json()
 assert new_user['name'] == 'Matias QA'
 assert 'id' in new_user and 'createdAt' in new_user

 #Endpoint_LOGIN
LOGIN_URL = 'https://reqres.in/api/login'
def test_login_successful():
 creds = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
 resp = requests.post(LOGIN_URL, json=creds)
 assert resp.status_code == 200
 assert 'token' in resp.json()

 #email + passwor correctos = codigo 200
 #si omitis uno de los dos = codigo 400 (bad request)