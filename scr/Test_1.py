import time
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from Funciones import FuncionesGlobales
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoAlertPresentException

def test_1():
    pelicula = input("Ingrese el nombre de la película: ")  # ingresamos la pelicula a buscar
    driver = webdriver.Chrome()     # conexion con el navegador
    f = FuncionesGlobales(driver)   # llamada de las fuciones
    f.navegar("https://www.imdb.com/")  # navegar a la pagina
    driver.maximize_window()    # maximiza la ventana
    time.sleep(2)
    f.texto_id("suggestion-search", pelicula)   # busqueda de la pelicula
    titulo_pelicula= f.extraer_titulo()     # extraccion del titulo de la pelicula
    contenido = f"Título encontrado: {titulo_pelicula}"     # guardamos la cadena en la variable contenido
    f.guardar_resultado(contenido, "resultado_test1.txt")   # guardamos el contenido en el archivo
    driver.quit()   # cierre del navegador

def test_2():
    pelicula = input("Ingrese el nombre de la película: ")  # ingresamos la pelicula a buscar
    driver = webdriver.Chrome()     # conexion con el navegador
    f = FuncionesGlobales(driver)   # llamada de las fuciones
    f.navegar("https://www.imdb.com/")      # navegar a la pagina
    driver.maximize_window()    # maximiza la ventana
    time.sleep(2)
    f.texto_id("suggestion-search", pelicula)   # busqueda de la pelicula
    titulo_pelicula = f.extraer_titulo()    # extraccion del titulo de la pelicula
    f.click_listado()   # click en listado desplegado de la busqueda
    time.sleep(2)
    puntaje = f.puntaje_pelicula()  # obtencion de rating de la pelicula
    generos = f.extraer_genero()    # obtencion de los generos de la pelicula
    # Modificamos la construcción de la cadena 'contenido'
    contenido = f"Título original: {titulo_pelicula}\nRating IMDB: {puntaje.split(': ')[1]}\nGéneros: "
    # puntaje.split(': ')[1] divide la cadena del rating y toma solo el número
    contenido += ", ".join(generos)  # Unimos los géneros con comas
    print(contenido)    # mostramos en pantalla el contenido de lo que se va a guardar
    f.guardar_resultado(contenido, "resultado_test2.txt")   # guardamos el contenido en el archivo
    driver.quit()   # cierre del navegador

# El flag -s permite que la función input() funcione correctamente en pytest.
if __name__ == "__main__":
    test_1()
    test_2()

