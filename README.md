# 🚀 Proyecto  Automation de Talento Tech

## 🎯 Propósito del proyecto
Este proyecto tiene como objetivo **automatizar pruebas de UI y API** para el sitio **SauceDemo**, aplicando buenas prácticas como:

- Page Object Model (POM)
- Manejo de datos externos (CSV / JSON)
- Generación automática de reportes HTML
- Logging centralizado
- Captura automática de pantallas ante fallos

> ✔️ La estructura está diseñada para mantener orden, escalabilidad y facilidad de mantenimiento.

---

## 🛠️ Tecnologías utilizadas
- **Python 3.x**
- **Pytest** → ejecución de pruebas
- **Selenium WebDriver** → automatización UI
- **jsonplaceholder** → pruebas de API
- **Faker** → generación de datos dinámicos
- **Logging**
- **CSV / JSON** para datos externos
- **GitHub Actions/CI** para una integracion continua y correr todas las pruebas cada vez que se hace un push

---

## 📊 Reportes y Logs

Durante la ejecución, el proyecto genera **tres tipos de resultados principales**:

### 📄 Reporte HTML
- Se genera automáticamente como:  
  ```reporte.html```
- Ubicación: **carpeta raíz del proyecto**
- Incluye:
  - Tests ejecutados  
  - Estado (OK / FAIL)  
  - Duración  
  - Capturas de pantalla  

---

### 📁 Logs de ejecución

Tambien se genera un log con informacion detallada de toda la ejecución de las pruebas en la siguiente ubicacion: ```logs/suite.log```

---

### 🖼️ Capturas de pantalla
- Se generan **solo cuando una prueba falla**.  
- Permiten revisar visualmente el estado del navegador al momento del fallo.

---

## ▶️ Ejecutar todas las pruebas

Ejecuta la suite completa con:

```bash
python -m run_tests
```
Esto lanzará todos los tests y generará automáticamente el reporte HTML, el log y las capturas.

## 📘 ¿Cómo interpretar los reportes?

Al ejecutar run_test.py, se genera un archivo HTML con:

✔️ Lista completa de pruebas

✔️ Estado de cada prueba

✔️ Duración

✔️ Screenshots en pruebas fallidas

Este reporte permite analizar rápidamente resultados y detectar errores.

## 🧪 Pruebas incluidas
🔐 Login

Login exitoso

Login fallido

Login con datos generados con Faker

📦 Inventario

Validación de productos en pantalla

Comportamiento al agregar items

🛒 Carrito

Agregar y eliminar productos

Validaciones de estado

🌐 API (JsonPlaceHolder)

GET users

POST create user

DELETE user

Validación de códigos HTTP

Validación de estructura JSON

## 📂 Manejo de datos de prueba

En la carpeta datos/ se incluyen archivos externos como:

data_login.csv → usuarios válidos e inválidos

productos.json → datos de productos para la UI

Esto permite separar la lógica del código de los datos, facilitando configuraciones y escalabilidad.

## 🧾 Conclusión

Este proyecto ofrece una arquitectura limpia, modular y escalable para automatizar pruebas con Python y Pytest.

Incluye:

Ejecución centralizada con run_test.py

Reporte HTML automático

Registro completo en logs

Buena organización de carpetas y datos

Permite agregar nuevos tests de forma simple sin alterar el núcleo del framework, garantizando buenas prácticas y extensibilidad en el tiempo.

Permite correr todas las pruebas cada vez que se hace una actualiza y asi detectar cualquiero posible error en el menor tiempo posible