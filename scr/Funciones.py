import time
import os
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import json

class FuncionesGlobales:

    def __init__(self, driver):
        self.driver = driver

    # Funcion para navegar a la pagina web
    def navegar(self, url):
        self.driver.get(url)
        print("Navego a la pagina: ", url)
        self.driver.maximize_window()

    def texto_id(self, elemento_id, texto):
        val = self.driver.find_element(By.ID, elemento_id)
        val.clear()
        val.send_keys(texto)
        print("Texto Id enviado correctamente: ", texto)
        val.send_keys(Keys.RETURN)
        time.sleep(2)   # Espera la carga de resultados

    def extraer_titulo(self):
        try:
            # Esperar hasta que cargue la lista de resultados
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//li[contains(@class, 'ipc-metadata-list-summary-item')]//a"))
            )
            titulo = self.driver.find_element(By.XPATH, "//li[contains(@class, 'ipc-metadata-list-summary-item')]//a")\
                .text
            print(f"Título encontrado: {titulo}")
            return titulo
        except:
            print("No se encontró el título de la película.")

    def click_listado(self):
        try:
            # Esperar hasta que cargue la lista de resultados
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//li[contains(@class, 'ipc-metadata-list-summary-item')]//a"))
            )
            titulo = self.driver.find_element(By.XPATH, "//li[contains(@class, 'ipc-metadata-list-summary-item')]//a")
            titulo.click()
            '''print(f"Título encontrado: {titulo}")
            return titulo'''
        except:
            print("No se encontró el elemento")

    def puntaje_pelicula(self):
        # Esperar a que cargue la página de la película y el script JSON-LD con el rating
        try:
            script_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//script[@type='application/ld+json']"))
            )
            script_content = script_element.get_attribute("innerText")

            # Extraer el JSON con el rating
            data = json.loads(script_content)
            rating = data.get("aggregateRating", {}).get("ratingValue", "No encontrado")
            return f"Ranking de la pelicula: {rating}"
        except TimeoutException:
            return f"No se pudo obtener el rating de la película."

    def extraer_genero(self):
        # Extraer el contenido del script con JSON-LD
        script_element = self.driver.find_element(By.XPATH, '//script[@type="application/ld+json"]')
        json_data = json.loads(script_element.get_attribute("innerText"))

        # Obtener los géneros
        generos = json_data.get("genre", [])
        return generos


    def guardar_resultado(self, contenido, archivo):
        os.makedirs("output", exist_ok=True)  # Crea la carpeta si no existe
        ruta = f"output/{archivo}"
        with open(ruta, "w", encoding="utf-8") as file:
            file.write(contenido)
            print(f"Resultado guardado en {archivo}")
