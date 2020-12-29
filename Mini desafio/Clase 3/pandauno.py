#-*- coding: utf-8 -*-
'''
Mini desafío 1.A
Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato. 
El archivo tiene dos columnas, Equipo y Puntos. 
Determinar de cada equipo la diferencia de gol (goles a favor - goles en contra), 
y mostrar todas las diferencias de gol con print
'''

import pandas as pdata

    archivo = pdata.read_excel("Tabla1.xlsx")

    data = archivo.to_dict("list")
# "list" significa que vamos a almacenar a cada columna como una lista con su contenido
    filas = len(data["Equipo"])

    print("Diferencias de gol:")

    for i in range(len(data["Equipo"])):
        print(data["Equipo"][i], ":", data["Goles a favor"][i] - data["Goles en contra"][i])

