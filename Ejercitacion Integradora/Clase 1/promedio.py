#-*- coding: utf-8 -*-
""" Cálculo de promedio 
Cálcular la nota de un alumno es una tarea cotidiana de un profesor.
 Esta tarea suele realizarse a mano o en excel muchas veces. En esta ocasión la haremos en python. 
- Escribir una función que calcule el promedio de 3 notas y entrege ese valor usando **return**.
- Reescribir la función anterior modificandola para asignar una importancia al primer examen de 20%, 
    al segundo de 50% y al tercero de 30%.
- Llamar a cada función anterior 3 veces con distintas notas y verificar, mediante la instrucción **if**, 
si el alumno aprobó en cada caso (suponga que 4 es la nota de aprobación).
"""


def promedio(n1,n2,n3):
    p=(n1+n2+n3)/3
    return p


def pimportante(n1,n2,n3):
    p=n1*0.2+n2*0.5+n3*0.3
    return p

if pimportante(3,4,5)>=4:
    print("Aprobado")
else:
    print("Desaprobado")

