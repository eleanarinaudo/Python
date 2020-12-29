#*-* coding:utf-8 *-*
'''
Las Naranjas de Miguel
Miguel vive en un pueblo frutero con su hermana en el valle de Oz. 
Todos los días cosecha bananas y naranjas de su campo. Como son abundantes, 
suele darle 2 bananas y 1 naranja a su hermana. 
No obstante Miguel siempre quiere quedarse con por lo menos una naranja, 
por lo cual le da una naranja a su hermana solo cuando se cosechan al menos 2 naranjas.

Miguel ahora quiere modernizarse, compró una cinta transportadora que detecta cada fruta que 
la atraviesa y te pide ayuda para escribir un programa que reciba el código generado por la máquina 
y devuelva la cantidad de bananas y naranjas que le quedarán a Miguel luego de quitar las frutas que
 le dará a su hermana.
'''


def cuantNaranjas_miguel(codigo):
    naranjas_miguel = 0
    for elemento in codigo:
            if elemento == "N":
                naranjas_miguel += 1
    if naranjas_miguel > 2:
        naranjas_miguel -= 1
    elif naranjas_miguel == 2:
        naranjas_miguel -= 1
    return naranjas_miguel

def cuanBananas_miguel(codigo):
    bananas_miguel = 0

    for elemento in codigo:
        if elemento == "B":
            bananas_miguel += 1
    if bananas_miguel > 1:
        bananas_miguel -= 2
    elif bananas_miguel == 1:
        bananas_miguel -= 1
    return bananas_miguel

codigo=input()
print(cuanBananas_miguel(codigo),cuantNaranjas_miguel(codigo))