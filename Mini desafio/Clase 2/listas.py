#-*- coding: utf-8 -*-

"""Ejercicios de listas
    Crear una lista con los números pares menores a 50.
    Crear una lista con el nombre de los días de la semana. 
Realizar un programa al cual se ingresa el día del año mediante un número de 0 a 364, 
que determine a qué día de la semana corresponde mediante un número de 0 (Lunes) a 6 (Domingo) 
y luego muestre en pantalla el elemento correspondiente de la lista
 (suponemos que el día 0 del año es Lunes).
    Realizar un programa que ordena nombres alfabeticamente. 
Primero debe pedir al usuario que ingrese el número de nombres que serán ingresados, 
luego debe pedir al usuario que ingrese un nombre y repetir ese pedido la cantidad de veces indicada.
 Los nombres se deben ir agregando a una lista. Por último, ordenar la lista alfabéticamente y mostrar 
 en pantalla de a uno por vez los nombres ordenados (usando un for).
"""

numero=[]
for i in range(50)
    if i % 2 == 0
        numero.append(i)
print(numero)



week=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
dayOfTheYear=int(input("Ingrese un dia del anio:"))
dayOfTheWeek=dayOfTheYear%7
print(week[dayofTheWeek])



cantNombres=int(input("Ingrese la cantidad de nombres que seran ingresados: "))
listNombres=[]

    for x in range cantNombres:
        mensaje="Ingrese el nombre #" + str(x+1) + " :"
        newNombres=input(mensaje)
        listNombres.append(newNombres)

    listNombres.sort()

    print("Los nombres ingresados son: ")
    for n in listanombre:
        print(n)
