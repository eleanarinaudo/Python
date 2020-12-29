#-*- coding: utf-8 -*-
"""#### #### Mini-desafío: floats
    Crear: 
*   Una función que convierta grados **Celsius** a grados **Farenheit** 
    (https://es.wikipedia.org/wiki/Grado_Fahrenheit)
*   Una función que convierta grados **Celsius** a grados **Kelvin** 
    (https://es.wikipedia.org/wiki/Kelvin)

    El usuario debe ingresar una temperatura en grados Celsius y 
    el programa debe mostrar las conversiones a Farenheit y Kelvin utilizando las funciones. 
    Si la temperatura ingresada es inferior al [cero absoluto]
    (https://es.wikipedia.org/wiki/Cero_absoluto), 
    el programa debe mostrar un mensaje de advertencia.

    Pueden leer [aqui](https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature)   
 sobre como hacer las conversiones.
"""


celsius=float(input("Ingrese una temperatura en grado Celsius: "))

def convertionFarenheit(celsius):
    resultado=celsius*9/5+32 
    if resultado < 0:
        print("ADVERTENCIA!")
    return resultado 

def convertionKelvin(celsius):
    resultado=celsius+273.15
    if resultado < 0:
        print("ADVERTENCIA!")
    return resultado



print('La conversion de C a F es:', convertionFarenheit(celsius))
print('La conversion de C a K es:', convertionKelvin(celsius))


