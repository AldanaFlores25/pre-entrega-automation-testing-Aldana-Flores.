import requests  # Importamos la librería para hacer solicitudes HTTP

# Encabezados personalizados que se envían con la petición
# (En ReqRes no son necesarios, pero esto simula una API real con autenticación)
encabezado = {
    "x-api-key": "reqres-free-v1"
}

# URL del endpoint al que vamos a enviar la solicitud
# En este caso, estamos consultando los datos del usuario con ID = 2
url = "https://reqres.in/api/users/2"

# Realizamos una solicitud HTTP GET para obtener información del usuario
# También enviamos los headers por si la API los necesita
response = requests.get(url, headers=encabezado)

# Imprimimos el código HTTP de la respuesta del servidor
# 200 significa que la solicitud fue exitosa
print(response.status_code)

# Convertimos el contenido de la respuesta en formato JSON a un diccionario de Python
data = response.json()

# Imprimimos el diccionario resultante, que contiene la información del usuario
print(data)
