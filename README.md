# Proyecto de Automatización con Selenium - Saucedemo

## Propósito del Proyecto
Este proyecto fue creado con fines educativos para practicar **automatización de pruebas funcionales** con Python y Selenium.  
Los casos de prueba se ejecutan sobre la página de demostración **[SauceDemo](https://www.saucedemo.com/)**, un sitio diseñado para probar flujos típicos de una tienda online (login, inventario, carrito, checkout, etc.).

Los objetivos principales son:
- Validar el funcionamiento del **login**.
- Verificar la **navegación y elementos del inventario**.
- Probar la **funcionalidad del carrito de compras**.
- Reutilizar funciones y aplicar buenas prácticas de automatización.

---

##  Tecnologías Utilizadas

|      Tecnología        |     Descripción           |
|------------------------|---------------------------|
| **Python 3.13+** | Lenguaje principal del proyecto |
| **Selenium 4.36+** | Librería para automatizar navegadores |
| **WebDriver** | Controlador del navegador (Edge o Chrome) |
| **EdgeDriver / ChromeDriver** | Permite a Selenium comunicarse con el navegador |
| **Pytest**         | Framework recomendado para ejecutar los tests de forma organizada |

---

## Instalación de Dependencias

1. **Clonar el proyecto (o descargar los archivos)**  
   ```bash
   git clone https://github.com/AldanaFlores25/PreEntrega-FloresAldana.git
   cd selenium-PreEntrega-FloresAldana

2. **instalar python (si no lo tenes)**
    desde: https://www.python.org/downloads/
 
3. **instalar selenium**
    desde la consola
    ## comando: pip install selenium

4. **instalar pytest**
    desde la consola
    ## comando: pip install pytest

5. **instalar webdriver**
    desde consola:
    ## comando: pip install webdriver-manager


## Ejecucion de los tests

1. *Abrir la terminal en la carpeta del proyecto*

2. *Ejecutar todos los tests con el comando:*
  **pytest**

3. *para ejecutar un test especifico:*
  **pytest tests/test_login.py**


## BUENAS PRACTICAS

 *Mantener los selectores organizados y actualizados.*

 *Reutilizar funciones con Page Objects o helpers.*

 *Documentar cada test con su propósito y resultado esperado.*