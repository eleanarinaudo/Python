#-*- coding: utf-8 -*-
"""Ejercicio de entrevista en Ingemática
Escriba un programa que imprima los números del 1 al 100, pero que para cada número
 que sea múltiplo de 3 imprima N3, para los múltiplos de 5 imprima N5, y para los múltiplos de los dos, 
 N3N5.

Tips
¡Si el número es divisible por 3 entonces el resto de la división vale cero!
numero % 3 == 0
>> True
"""

for i in range(1,100):
    if i%3==0 and i%5==0:
        print("N5N3")
    elif i%3==0:
        print("N3")
    elif i%5==0:
        print("N5")
    else:
        print(i)