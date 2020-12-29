#-*- coding: utf-8 -*-
'''
¿Acaso hubo buhos aca?
Definir una función que detecte si una palabra es un palíndromo y devuelve True o False.

Ejemplos:

palindromo( "python" ) => False

palindromo( "reconocer" ) => True

palindromo( "Neuquén" ) => False

★★ Challenge: Modificar la función para ignorar espacios, signos de puntuación,
 y que no haga distinción entre mayúsculas y minúsculas (pueden usar str.lower). 
 Sugerimos usar el nombre del desafío como un palindromo de ejemplo.

'''


def palidromo (texto):
    return texto==texto[::-1]

print(palidromo("python"))
print(palidromo("reconocer"))
print(palidromo("Neuquén"))