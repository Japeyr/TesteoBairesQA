Este programa automatiza la búsqueda de películas en IMDB, extrayendo información como el título, el ranking y los géneros.

## Descripción del Proceso

1.  **Extracción del ZIP:** Descomprime el archivo ZIP que contiene los archivos del programa.
2.  **Navegación:** El script abre un navegador Chrome y navega a la página principal de IMDB.
3.  **Búsqueda:** Se ingresa el nombre de una película a través de la interfaz de usuario, y el script realiza la búsqueda en el sitio.La búsqueda de la película se realiza utilizando la función texto_id() dentro de la clase FuncionesGlobales, ubicada en el archivo Funciones.py. Esta misma función es utilizada en ambos tests para garantizar modularidad y evitar duplicación de código.
4.  **Extracción de Datos:**
    * Se extrae el título de la película del primer resultado de la búsqueda.
    * Se hace clic en el primer resultado para acceder a la página de la película.
    * Se extrae el ranking de IMDB y los géneros de la película utilizando datos JSON-LD presentes en la página.
5.  **Guardado de Resultados:** Los datos extraídos se guardan en archivos de texto (`resultado_test1.txt` y `resultado_test2.txt`).

## Instrucciones de Ejecución

1.  **Descomprimir el ZIP:** Extrae los archivos del archivo ZIP a una carpeta en tu sistema.
2.  **Instalar Python:** Asegúrate de tener Python 3.11.2 instalado en tu sistema. Puedes descargarlo desde [https://www.python.org/downloads/](https://www.python.org/downloads/). Durante la instalación, asegúrate de marcar la casilla "Add Python to PATH" para que Python sea accesible desde la línea de comandos.
3.  **Instalar dependencias:** Abre una ventana de comandos (CMD) y ejecuta el siguiente comando para instalar las dependencias necesarias:

    ```bash
    pip install selenium pytest
    ```

4.  **Descargar ChromeDriver:**
    * Asegúrate de tener la versión de Google Chrome: 134.0.6998.119 (Build oficial) (64 bits) (cohort: Control).
    * Ve a [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) y descarga el ChromeDriver que coincida con esta versión de Chrome.
    * Coloca el ejecutable de ChromeDriver en un directorio incluido en tu PATH, o especifica la ruta al ejecutable en el código.
5.  **Ejecutar las pruebas:** Abre una ventana de comandos (CMD), navega al directorio donde descomprimiste los archivos y ejecuta el siguiente comando:

    ```bash
    pytest Test_1.py -s
    ```

    * El flag `-s` es necesario para permitir la entrada de datos a través de `input()`.

## Dependencias

* `selenium`: Para la automatización del navegador.
* `pytest`: Para la ejecución de pruebas.
* `ChromeDriver`: Para controlar el navegador Chrome (versión 134.0.6998.119).

## Consideraciones importantes

* **Rutas de archivo:** El script `ejecucion.bat` contiene rutas de archivo específicas de mi sistema. Es posible que debas modificar estas rutas para que coincidan con la ubicación de tus archivos.
* **Variables de entorno:** Asegúrate de que las rutas de Python y ChromeDriver estén incluidas en tu variable de entorno `PATH`.
* **Limitaciones de portabilidad:** Este script depende de Python, `pytest` y ChromeDriver, que deben estar instalados en el sistema donde se ejecuta. Debido a estas dependencias externas y las diferencias en los sistemas operativos, la portabilidad completa del script puede ser difícil.
* **Posibles problemas:** Si tienes problemas para ejecutar el script, asegúrate de haber seguido todos los pasos de instalación correctamente y de que las rutas de archivo y las variables de entorno estén configuradas correctamente.

Modificación del script ejecucion.bat
El archivo ejecucion.bat contiene rutas específicas de mi sistema. Para adaptarlo a otro entorno, el usuario debe:

Asegurarse de que Python y ChromeDriver estén correctamente instalados.

Modificar la ruta a Python si es necesario. Para verificar la ruta en Windows, ejecutar en la terminal:

```bash
where Python
```
Si ChromeDriver no está en el PATH, modificar la línea donde se especifica su ubicación.

Si se desea ejecutar desde otro directorio, cambiar la ruta del archivo de prueba (Test_1.py).

Nota: En la consigna se menciona que se prefiere Playwright, pero dado que mi experiencia es con Selenium, elegí utilizarlo para completar el ejercicio.