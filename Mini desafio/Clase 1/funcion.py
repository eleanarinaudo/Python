#-*- coding: utf-8 -*-
"""#### Mini-desafío funciones
Escribir una función que chequee los siguientes usuarios y contraseñas:

Usuario: Juan - Contraseña: 12345_
Usuario: Pablo - Contraseña: xDcFvGbHn
La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.
"""

def acceso(usuario, pw):
    
    if (usuario=="Juan" and pw=="12345_") or (usuario=="Pablo" and pw=="xDcFvGbHn"):
        resultado=True
    else:
        resultado=False
    return resultado
   
usuario=input("Ingrese el nombre del usuario: ")
pw= input("Ingrese la contrasenia: ")

login=acceso(usuario,pw) 
print(login)