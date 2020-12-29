#-*- coding: utf-8 -*- 
""" Test de primalidad 
Escribir una función que recibe un numero y devuelve *True* si el numero es primo y *False* en caso contrario.

Mediante un *for* verificar la *primalidad* de los numeros del $1$ al $20$.

**Tips**

* Un número $N$ es primo cuando tiene exactamente $2$ divisores ($1$ y $N$). 
Sin embargo alcanza con verificar que no es múltiplo de ningún número entre $2$ y $\sqrt{N}$ 
(recordar que $\sqrt{N}=N^{0.5}$)
* El numero 1 **no** es primo.
"""

def esPrimo(n):
    if n==1:
        return False
    d=d+1
    else:
        return True

for x in range (1,21):
    print (x, "es primo?", esPrimo(x))
