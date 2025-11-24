import requests  # Importamos la librería para hacer solicitudes HTTP

# Endpoint de la API al que vamos a enviar la solicitud
# En este caso, estamos modificando (actualizando) el usuario con ID 2
url = "https://reqres.in/api/users/2"

# Encabezados personalizados que enviamos con la petición.
# ReqRes no los necesita realmente, pero esto simula una API real con autenticación
encabezado = {
    "x-api-key": "reqres-free-v1"
}

# Datos que deseamos actualizar en el usuario
# Aquí estamos cambiando solamente el campo "name"
data = {
    "name": "Jose"
}

# Enviamos una petición HTTP PATCH
# PATCH se usa para modificar parcialmente un recurso (no reemplazarlo completamente)
response = requests.patch(
    url,
    headers=encabezado,
    json=data    # Enviamos los datos como JSON
)

# Imprimimos el código de respuesta del servidor
# 200 significa que la actualización fue exitosa
print(response.status_code)

# Convertimos la respuesta del servidor a JSON y la mostramos
# Normalmente devolverá los datos modificados y una fecha de actualización
print(response.json())
