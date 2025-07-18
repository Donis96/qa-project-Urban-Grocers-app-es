# Proyecto Urban Grocers 
Este proyecto contiene una suite de pruebas automatizadas para la API de Urban Grocers, enfocándose en la validación de diversas funcionalidades, incluyendo casos positivos y negativo

Descripcion del proyecto
El objetivo principal de este proyecto es realizar una serie de pruebas positivas y negativas sobre la API de Urban Grocers. Estas pruebas buscan asegurar la correcta funcionalidad del servicio, verificando tanto que la API se comporta como se espera ante entradas válidas, como que maneja adecuadamente los escenarios de error y las entradas inválidas.

Nota Importante: Algunas pruebas están diseñadas intencionadamente para fallar (por ejemplo, devolviendo un código de estado 400 Bad Request). Este es el comportamiento esperado para validar los casos negativos, lo que confirma que la API rechaza correctamente las solicitudes que no cumplen con sus validaciones. Un FAILED en estos escenarios significa que la validación de la API está funcionando correctamente.

Requisitos Previos
Asegúrate de tener instalado Python 3.13.3 o superior en tu sistema.

Necesitarás las siguientes librerías de Python. Puedes instalarlas usando pip: bash, pip install pytest requests


¡Excelente! Con la información que me proporcionaste, puedo crear un README.md robusto y claro para tu proyecto "Urban Grocers".

Proyecto Urban Grocers: Automatización de Pruebas de API
Este proyecto contiene una suite de pruebas automatizadas para la API de Urban Grocers, enfocándose en la validación de diversas funcionalidades, incluyendo casos positivos y negativos.

Descripción del Proyecto
El objetivo principal de este proyecto es realizar una serie de pruebas positivas y negativas sobre la API de Urban Grocers. Estas pruebas buscan asegurar la correcta funcionalidad del servicio, verificando tanto que la API se comporta como se espera ante entradas válidas, como que maneja adecuadamente los escenarios de error y las entradas inválidas.

Nota Importante: Algunas pruebas están diseñadas intencionadamente para fallar (por ejemplo, devolviendo un código de estado 400 Bad Request). Este es el comportamiento esperado para validar los casos negativos, lo que confirma que la API rechaza correctamente las solicitudes que no cumplen con sus validaciones. Un FAILED en estos escenarios significa que la validación de la API está funcionando correctamente.

Requisitos Previos
Asegúrate de tener instalado Python 3.13.3 o superior en tu sistema.

Necesitarás las siguientes librerías de Python. Puedes instalarlas usando pip:

Bash

pip install pytest requests
Estructura de Archivos
El proyecto está organizado en los siguientes archivos clave:

configuration.py: Contiene la URL base del servicio API y las rutas de los endpoints.

data.py: Almacena los cuerpos (payloads) de las solicitudes JSON y otros datos de prueba utilizados en los tests.

sender_stand_request.py: Módulo que encapsula las funciones para enviar solicitudes HTTP (POST, GET, etc.) a la API utilizando la librería requests.

create_kit_name_kit_test.py: Contiene todas las definiciones de las pruebas automatizadas para la creación de kits y otros escenarios de la API.

README.md: Este archivo, que proporciona una descripción del proyecto y las instrucciones para su ejecución.

.gitignore: Define los archivos y directorios que Git debe ignorar al gestionar el control de versiones.


