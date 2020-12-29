# *-* coding:UTF-8 *-*
"""###$\medio$  Dominó  

El [Dominó]es un juego de mesa muy popular. 
En este ejercicio no vamos a programar un juego de Domino, pero sí contar sus fichas.

<img src="https://es.calcuworld.com/wp-content/uploads/sites/2/2018/04/cantidad-de-fichas-domino.jpg" height="200" alt = "Fichas domino desparramadas sobre una mesa">

A pesar de que el domino tradicional se juega con fichas hasta el número 6, vamos a considerar un juego de fichas de valor máximo $n$.

- Escribir una función que calcule la cantidad de fichas para un juego de dominó completo con fichas que contienen hasta el número $n$.
Nota: ¡No hay fichas repetidas! 2-4 es la misma ficha que 4-2. ¡Observar que en el dominó hay fichas con valor 0!

```
   cantidadFichas(3)
   >>> 10
   cantidadFichas(4)
   >>> 15
```
"""

def cantidadFichas(n):
    print((n+1)*(n+2)//2)
    
def mostrarFichas(n):
    for i in range(0,n+1):
        for j in range(i,n+1):
            print(str(i)+'-'+str(j))
            
def valorMaximo(num):
    n = 1
    while (n+1)*(n+2)/2 < num:
        n+=1
    if (n+1)*(n+2)/2 == num:
        print(n)
    else:
        print(-1)
print("CantidadFichas(3)")
cantidadFichas(3)