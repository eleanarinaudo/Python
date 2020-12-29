#-*- coding: utf-8 -*-
'''
Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato y 
determinar qué equipo es el campeón (1ro) y perdedor (último).
El archivo tiene dos columnas, Equipo y Puntos
'''

import pandas as import pdata

    archivo = pd.read_excel("Datos.xlsx", index_colum="Equipo") 
    data = archivo.to_dict("index")


    maxpto=0
    minpto=10000000
    maxname=""
    minname=""


 
    for i in data.i():
      pto=data[i]["Puntos"]
        if pto>maxpto:
            maxpto=pto
            maxname=i 

        if pto<minpto:
            min_pto=pto
            minname=i


    print(maxname, " resulto campeon con ", maxpto, " puntos.")
    print(minname, " resulto campeon con ", minpto, " puntos.")