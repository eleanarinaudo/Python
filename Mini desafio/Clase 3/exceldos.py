#*-* coding: utf-8 *-*
'''
### **Mini desafío 2.B**

Escribir una funcion que reciba como parámetros: una variable de tipo **DataFrame** 
(la tabla de alumnos) y el índice de un alumno. 
Luego debe devolver con *return* el promedio de sus notas en las diferentes materias.
'''

import pandas as pd

def promedio(df, indice):
    alumno = datos.loc[indice] 
    m= alumno["Matematica"]
    f= alumno["Fisica"]
    q=alumno[ "Quimica"]
   return sum (m + f +q )/ 3

datos = pd.read_excel("Datos.xlsx")

print("El promedio del dato 0 es %0.2f " % promedio(datos, 0))
print("El promedio del dato 1 es %0.2f " % promedio(datos, 1))
