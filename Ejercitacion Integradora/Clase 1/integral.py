#-*- coding:utf-8 -*-
"""
### El ejercicio más integrador

Se pide calcular una integral definida en un intervalo de una función genérica.

En lugar de obtener un resultado exacto, realizaremos una aproximación del resultado aplicando la integral de Riemann. Para lograr esto vamos a aproximar una función mediante muchos rectángulos muy angostos. Para obtener el resultado de la integral vamos a sumar el área de todos estos rectángulos entre cierto intervalo $[a, b]$:

![Riemann1](https://upload.wikimedia.org/wikipedia/commons/a/af/Riemann_Integration_4.png)

Primero debemos elegir un número $\Delta x$ cuyo valor sea muy pequeño, y que determina el ancho de los rectángulos. Comenzando del límite de integración inferior $a$ obtendremos el primer área como $f(a)\cdot \Delta x$, luego el siguiente área será $f(a+\Delta x)\cdot \Delta x$ , el tercer área es $f(a+2\cdot\Delta x)\cdot \Delta x$ , y así se sigue mientras no se supere $b$.

Al elegir un valor más chico de $\Delta x$ se obtiene una mejor aproximación:

![Riemann2](https://upload.wikimedia.org/wikipedia/commons/3/34/Riemann_Integration_5.png)

Se debe programar la función *integral(f, a, b, dx)* en la cual *f* sea la función a integrar (debe recibir como parámetro un número *x*, debe entregar el resultado usando *return*), *a* y *b* sean los límites de integración, y *dx* sea el ancho de los rectángulos.


"""


def f1(x):
      return 1

def f2(x):
  return x

def f3(x):
  return x**2 - 3*x

def integral(f, a, b, dx):
  resultado = 0
  x = a
  while (x + dx) <= b:
    resultado += f(x) * dx
    x += dx
  return resultado
