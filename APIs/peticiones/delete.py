import requests  # Librería para realizar solicitudes HTTP

# Encabezados opcionales que se envían junto con la petición
# En este caso se incluye una API KEY de ejemplo (aunque ReqRes no la necesita realmente)
encabezado = {
    "x-api-key": "reqres-free-v1"
}

# URL del recurso que queremos eliminar (usuario con ID = 2)
url = "https://reqres.in/api/users/2"

# Realizamos una solicitud HTTP DELETE al servidor
# Indicando también los encabezados (headers)
response = requests.delete(url, headers=encabezado)

# Mostramos el código de respuesta HTTP
# En ReqRes, la eliminación exitosa devuelve 204 No Content
print(response.status_code)

# Mostramos el contenido de la respuesta
# En esta API normalmente estará vacío, ya que 204 = sin contenido
print(response.text)
