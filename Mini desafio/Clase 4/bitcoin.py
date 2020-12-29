#*-* coding:utf-8 *-*
'''
Mini desafío 2.A
Se pide realizar un gráfico del valor del Bitcoin de los últimos 10 años, 
marcar con un punto el valor máximo del gráfico, calcular cuándo sucedió.

Nota:

Usen la función read_csv. Un .csv es prácticamente idéntico a un .xlsx.
Los valores a graficar estan la columna "Open" (usando to_dict("list") podrían resolver el problema).
'''


# Importamos la libreria requests
import requests

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
# Como usarla
wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/BTC.csv")
#Datos extraidos desde https://es.finance.yahoo.com/

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import time

archivo = pd.read_csv("BTC.csv")
data = archivo.to_dict("list")
cant = len(data["Date"])
x = []
y = []

precio_mas_alto = 0
dia_del_record = ""

for i in range(cant):
  x.append(data["Date"][i])
  y.append(data["Open"][i])

  if y[i] > precio_mas_alto:
    precio_mas_alto = y[i]
    dia_del_record = x[i]

print("El precio mas alto es:", precio_mas_alto)
print("Sucedio el dia:", dia_del_record)
record_label = 'Precio Record: {}\nDía del record: {}'.format(precio_mas_alto, dia_del_record)

plt.figure(figsize=(12, 4))
plt.plot(x, y)
plt.plot(dia_del_record, precio_mas_alto, 'ko', label=record_label)
plt.xticks(x[ : :200]) # Mostrar una de cada 200 fechas
plt.grid( axis='y' )   # Mostrar una grilla horizontal
plt.legend()           # Mostrar labels
plt.show()