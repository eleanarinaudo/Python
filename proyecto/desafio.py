#*-*coding: utf-8 *-*
'''
# Opción 1: Graficador de casos del COVID-19
Análisis y visualización de datos sobre los casos de coronavirus en distintos países.

En esta era de la desinformación puede resultar útil poder sacar uno mismo sus propias conclusiones 
 acerca de los datos presentados. 
El objetivo de este trabajo es obtener datos de casos y muertes por el Coronavirus de un repositorio de datos
 online y graficar por país.

Funcionalidad mínima (requisito):

La aplicación debe recibir del usuario el nombre del país deseado y
 permitir graficar casos detectados y fallecimientos totales para ese país en función del tiempo.
El usuario debe poder ingresar 2 países y 
 se permite graficar para dichos países la cantidad de casos y fallecimientos en dos gráficos con labels.
 El usuario debe poder ingresar el intervalo de tiempo a graficar. Calcular las intersecciónes 
 entre gráficos si las hubiera y marcarlas con un punto de algún tipo.
El usuario debe poder ingresar n países y
 se permite graficar para dichos países la cantidad de casos en una escala logaritmica.
  El programa debe pedirle al usuario el intervalo de tiempo deseado.
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget("https://covid.ourworldindata.org/data/ecdc/full_data.csv")

#Descarga de datos, casteo a Dataframe, elimino columnas innecesarias (faltaria eliminar los nan)
dataframe = pd.read_csv("full_data.csv")
dataframe = dataframe.drop(["weekly_cases","weekly_deaths","biweekly_cases","biweekly_deaths"],1)
lista = dataframe.to_dict("list")
lista_dic_paises = []

#Armo una lista con todos los paises incluidos en la DataFrame:
lista_locations = []
for pais in lista ["location"]:
  if pais not in lista_locations:
    lista_locations.append(pais)

#Función que hace diccionarios de los datos del pais ingresado:def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_3_datos/Datos.xlsx")
def diccionario_pais(pais_ingresado):
  a = 0
  c = 0
  for pais in lista["location"]:
    if a == 0:
      if pais_ingresado == pais :
        min_index = c
        a += 1
    elif a != 0: 
      if pais_ingresado != pais:
        if pais_anterior == pais_ingresado:
          max_index = c
    pais_anterior = pais
    c += 1

  diccionario_pais = {
      "date":[lista["date"][min_index:max_index]],
      "new_cases":[lista["new_cases"][min_index:max_index]],
      "new_deaths":[lista["new_deaths"][min_index:max_index]],
      "total_cases":[lista["total_cases"][min_index:max_index]],
      "total_deaths":[lista["total_deaths"][min_index:max_index]]
      }
  return diccionario_pais


#Input usuario
lista_paises_ingresados = []
while 1:
  pais_input = input ("Ingrese el pais, para finalizar ingrese finalizar:")
  if pais_input == "Finalizar" or pais_input == "finalizar":
    break
  if pais_input in lista_locations:
    lista_paises_ingresados.append(pais_input)
  else:
    print ("Pais no encontrado.")

for pais in lista_paises:
  j = diccionario_pais(pais)
  print (j)








#Descarga de datos, casteo a Dataframe, elimino columnas innecesarias (faltaria eliminar los nan)
!wget 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'
dataframe = pd.read_csv("full_data.csv")
dataframe = dataframe.drop(["weekly_cases","weekly_deaths","biweekly_cases","biweekly_deaths"],1)
lista = dataframe.to_dict("list")
lista_dic_paises = []

#Armo una lista con todos los paises incluidos en la DataFrame:
lista_locations = []
for pais in lista ["location"]:
  if pais not in lista_locations:
    lista_locations.append(pais)

#Función que hace diccionarios de los datos del pais ingresado:
def diccionario_pais(pais_ingresado):
  a = 0
  c = 0
  for pais in lista["location"]:
    if a == 0:
      if pais_ingresado == pais :
        min_index = c
        a += 1
    elif a != 0: 
      if pais_ingresado != pais:
        if pais_anterior == pais_ingresado:
          max_index = c
    pais_anterior = pais
    c += 1
  diccionario_pais = {
      "date":[lista["date"][min_index:max_index]],
      "new_cases":[lista["new_cases"][min_index:max_index]],
      "new_deaths":[lista["new_deaths"][min_index:max_index]],
      "total_cases":[lista["total_cases"][min_index:max_index]],
      "total_deaths":[lista["total_deaths"][min_index:max_index]]
      }
  return diccionario_pais
#Input usuario
lista_paises_ingresados = []
while 1:
  pais_input = input ("Ingrese el pais, para finalizar ingrese finalizar:")
  if pais_input == "Finalizar" or pais_input == "finalizar":
    break
  if pais_input in lista_locations:
    lista_paises_ingresados.append(pais_input)
  else:
    print ("Pais no encontrado.")

for pais in lista_paises:
  j = diccionario_pais(pais)
  print (j)





def funcion_diccionario(pais_ingresado):
  global min_index
  global max_index
  a = 0
  c = 0
  for pais in lista["location"]:
    if a == 0:
      if pais_ingresado == pais :
        min_index = c
        a += 1
    elif a != 0: 
      if pais_ingresado != pais:
        if pais_anterior == pais_ingresado:
          max_index = c
    pais_anterior = pais
    c += 1
  diccionario_pais = {
      "date":[lista["date"][min_index:max_index]],
      "new_cases":[lista["new_cases"][min_index:max_index]],
      "new_deaths":[lista["new_deaths"][min_index:max_index]],
      "total_cases":[lista["total_cases"][min_index:max_index]],
      "total_deaths":[lista["total_deaths"][min_index:max_index]]
      }
  return diccionario_pais






