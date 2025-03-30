Automatización de Búsqueda en IMDb para BairesQA

Este proyecto es una automatización de la búsqueda de películas en IMDb como parte de una prueba técnica para BairesQA. Utiliza Selenium y pytest para interactuar con el sitio web y extraer información relevante de las películas.

<br>
📝 Descripción del Proyecto

El programa automatiza la búsqueda de películas en IMDb, extrayendo y guardando información como:

✅ Título

✅ Ranking en IMDb

✅ Géneros

<br>
🔍 Proceso de Automatización

1. Descompresión del ZIP: Extrae los archivos en una carpeta local.

2. Navegación: Se abre un navegador Chrome y se accede a IMDb.

3. Búsqueda de película:

     ✅ Se ingresa el nombre de una película.

     ✅ La búsqueda se realiza mediante la función texto_id() dentro de la clase FuncionesGlobales en el archivo Funciones.py.

4. Extracción de datos:

     ✅ Se obtiene el título de la primera película en los resultados.

     ✅ Se accede a la página de la película para extraer su ranking y géneros desde datos JSON-LD.

5. Guardado de resultados: Se almacenan en archivos resultado_test1.txt y resultado_test2.txt.

<br>
🚀 Instrucciones de Instalación y Ejecución

📌 Requisitos Previos

✅ Python 3.11.2 (Descargar desde aquí). Asegúrate de marcar la opción "Add Python to PATH".

✅ Google Chrome (Versión 134.0.6998.119)

✅ ChromeDriver correspondiente a la versión de Chrome (Descargar desde aquí).

<br>
📥 Instalación

1. Instalar las dependencias ejecutando en la terminal:

pip install selenium pytest

2. Descargar ChromeDriver y colocarlo en un directorio dentro del PATH o especificar su ubicación en el código.

<br>
▶️ Ejecución de las Pruebas

✅ Abrir una terminal y navegar hasta la carpeta del proyecto.

✅ Ejecutar el siguiente comando:

      pytest Test_1.py -s

      El flag -s permite la entrada de datos mediante input().

<br>
📌 Consideraciones

✅ Rutas de archivo: El script ejecucion.bat contiene rutas específicas que pueden necesitar ajustes según el sistema del usuario.

✅ Variables de entorno: Asegurar que las rutas de Python y ChromeDriver estén en PATH.

✅ Posibles problemas:

✅ Verificar que todas las dependencias estén correctamente instaladas.

✅ Confirmar que las rutas y variables de entorno estén bien configuradas.

<br>
❗ Nota Importante

En la consigna se sugirió el uso de Playwright, pero dado que mi experiencia es con Selenium, elegí utilizarlo para completar la prueba.

<br>
📌 Autor: Jorge Peyrano
<br>
📅 Prueba Técnica para BairesQA
