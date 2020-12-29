#-*- coding: utf-8 -*-
#  Locos por las matemáticas: 
"""En marzo 2019, Emma Haruka Iwao, una empleada de Google, logró calcular 31,4 trillones de dígitos del famoso número pi en 121 dias usando el poder de la nube de Google. ¡Hoy ustedes pueden hacer lo mismo con la ayuda de Python!

Aprovechando el descubrimiento del matemático indio Sriniviasa Ramanujan (1910) podemos emplear nuestro propio aproximador de pi.
1π=22–√9801∑k=0∞(4k)!⋅(1103+26390k)(k!)43964k 

Pueden utilizar la siguiente función para calcular factoriales:

def factorial(n):
  if n<=1:
    return 1
  else:
    return n*factorial(n-1)
factorial(4)=4!=24 

Si no estamos tan locos por la matemáticas podemos usar otras aproximaciones más simples como

π≈227≈355113 

Otros números famosos:
e=∑k=0∞1k!e=limx→∞(1+1x)xφ=1+5–√2

"""



def factorial(n): # esto es una función iterativa
    rta = 1 # variable donde almacenaremos la respuesta
    for i in range(1, n+1):
        rta *= i
    return rta
    
def piApprox(num): 
    mul = 2**(3/2)/9801
    suma = 0
    for k in range(num):
        suma += factorial(4*k) /factorial(k)**4 *(1103+26390*k)/396**(4*k)
    return 1/(mul*suma)

print(piApprox(10))