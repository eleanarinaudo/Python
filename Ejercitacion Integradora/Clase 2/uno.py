#-*- coding: utf-8 -*-
'''
### $\facil$ Call me $\frac{\partial}{\partial x}$, or $\mathrm{diff}$ for short
Una operacion muy comun al manejar datos es la derivada

$$ \frac{d }{dt} (\mathrm{Datos}) $$

Objetivo: Escribir una funcion que tome una lista de $n$ numeros y devuelva la *derivada discreta* de la lista de tamano $n-1$.

Tips
* $\mathrm{derivada}[i]=x[i+1]-x[i]$ 

'''

def derivada(x):
    return [x[i]-x[i-1] for i in range(1,len(x))]

z=[2,3,4]
print(derivada(z))