#-*- coding: utf-8 -*-
'''
La conjetura del Dr. Lothar
Escriba un programa que reciba un n del usuario y repita el siguiente proceso usando un while:

Si el n es par, se debe dividir por  2 .
Si el n es impar, se debe multiplicar por  3  y sumar  1 .
Este proceso se repite hasta llegar al n  1  y luego muestra en pantalla la cantidad de pasos que tardó en llegar.

Ejemplos:

Input: 6

Output: 8 (Los pasos a seguir son: 6, 3, 10, 5, 16, 8, 4, 2, 1)

Input: 13

Output: 9 (Los pasos a seguir son: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1)
'''

n=int(input())

cantN=0
while n !=1:
    if n%2==0:
        n=n/2


    else:
        n=n*3 + 1

    cantN=cantN+1

print( cantN )






