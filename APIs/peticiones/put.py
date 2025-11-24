import requests  # Importamos la librería requests para hacer peticiones HTTP

# Encabezado que se enviará en la petición.
# En este caso incluye una clave de API que el servicio puede requerir para autorizar la solicitud.
encabezado = {"x-api-key": "reqres-free-v1"}

# URL del endpoint que queremos actualizar con método PUT.
# El usuario con ID 2 será actualizado.
url = "https://reqres.in/api/users/2"

# Datos que queremos enviar en el cuerpo de la petición.
# Representan los nuevos valores con los que vamos a actualizar al usuario.
data = {"name": "Valentina", "job": "Tutora"}

# Realizamos la solicitud PUT al servidor.
# - url: endpoint al que enviamos la petición
# - headers: enviamos el encabezado con la API key
# - json: enviamos el cuerpo de la petición en formato JSON
response = requests.put(url, headers=encabezado, json=data)

# Mostramos el código de respuesta HTTP.
# 200 indica éxito en la actualización.
print(response.status_code)

# Mostramos el contenido de la respuesta en formato JSON,
# que normalmente incluye los datos actualizados y metadatos como fecha de modificación.
print(response.json())
