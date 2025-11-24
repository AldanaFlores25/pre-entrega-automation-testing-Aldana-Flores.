import requests  # Librería para realizar solicitudes HTTP

# Encabezados que enviamos con la solicitud.
# Aunque ReqRes no los exige, simulan un entorno de API real con autenticación
encabezado = {
    "x-api-key": "reqres-free-v1"
}

# Endpoint donde queremos crear un nuevo usuario
url = "https://reqres.in/api/users"

# Datos del nuevo usuario que vamos a enviar a la API
data = {
    "name": "Jose",       # Nombre del usuario
    "job": "Profesor"     # Profesión del usuario
}

# Hacemos una solicitud POST
# POST sirve para crear nuevos recursos en el servidor
response = requests.post(
    url,
    headers=encabezado,   # Enviamos los headers
    json=data             # Mandamos el body del request como JSON
)

# Mostramos el código de estado de la respuesta
# Si es 201, significa que el recurso se creó correctamente
print(response.status_code)

# Convertimos la respuesta en JSON e imprimimos el contenido
# Normalmente devuelve el id del nuevo usuario y fecha de creación
print(response.json())
