
#-*- coding: utf-8 -*-
'''Mini-desafío: Diccionario²
Se recibieron distintos postulantes para un empleo de traductor. Crear un diccionario en el cuál la key de cada elemento sea el nombre de un candidato y el contenido sea un diccionario de los idiomas que aprendió. Para armar el diccionario de idiomas de cada candidato, los elementos deben tener como key el nombre del idioma y como contenido el valor True o False para los siguientes idiomas: Español, Ingles, Chino, Frances, Italiano.

Ejemplo del diccionario de idiomas:

{"Español":True, "Ingles":True, "Chino":False, "Frances":False, "Italiano":True}
Inventar valores para 5 candidatos.

El usuario luego debe poder ingresar el nombre de un idioma y el programa deberá mostrar en pantalla el nombre de aquellos candidatos que aprendieron ese idioma.'''


postulante={
    "Donald":{"Español":True, "Ingles":True, "Chino":False, "Frances":False, "Italiano":True,}
    "Peggy":{"Español":False, "Ingles":False, "Chino":True, "Frances":False, "Italiano":True},
    "Roger":{"Español":True, "Ingles":True, "Chino":False, "Frances":False, "Italiano":False},
    "Joan":{"Español":False, "Ingles":False, "Chino":True, "Frances":False, "Italiano":True},
    "Peter":{"Español":True, "Ingles":True, "Chino":False, "Frances":False, "Italiano":True}
}

idioma=input("Ingrese el nombre de un idioma:")

print("Los siguientes postulantes que aprendieron ese idioma:")

#Recorro todos los postulantes
for k in postulantes:
    dic_idioma=postulantes[k]
    if dic_idioma[idioma]==True:
        print(k)