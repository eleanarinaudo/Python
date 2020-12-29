#*-* coding: utf-8 *-*
'''
 **Mini desafío 4.B** - Challenge
Encontrar la palabra con mayor numero de ocurrencias en el texto de la noticia.
'''


conjuntoPalabras = set(palabras) # set con las palabras una sola vez cada una

ocurrenciaPalabras = {} # diccionario que almacenara la ocurrencia de las palabras

for palabra in conjuntoPalabras: # observar que itero conjuntoPalabras, es decir cada palabra distinta una sola vez
    ocurrenciaPalabras[palabra] = 0 # inciializamos la cantidad de ocurrencias de cada palabra

for palabra in palabras: # observar que itero la variable palabras, es decir, contando las palabras repetidas
    ocurrenciaPalabras[palabra] += 1 # incremento en uno la ocurrencia de la palabra

mayorOcurrencia = -1 # variable auxiliar para almacenar el numero de ocurrencias de la palabra más ocurrente
palabraMayorOcurrencia = -1 # variable auxiliar para almacenar la palabra de mayor ocurrencia
# No se relevante el valor de las dos variables anteriores

for palabra in ocurrenciaPalabras:
    # si todavia no registre palabras (mayorOcurrencia == -1) o encontre una palabra con mayor cantidad de ocurrencias que la anterior
    if mayorOcurrencia == -1 or ocurrenciaPalabras[palabra] > mayorOcurrencia: 
        # reemplazo la palabra con más ocurrencias y su cantidad de ocurrencias por los nuevos valores encontrados
        palabraMayorOcurrencia = palabra
        mayorOcurrencia = ocurrenciaPalabras[palabra]

print(palabraMayorOcurrencia)
print(mayorOcurrencia)