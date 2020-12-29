#*-* coding: utf-8 *-*
'''
Paréntesis balanceados
En este desafío deben programar un linter que verifique la correcta utilización de los paréntesis en un texto.

La entrada del programa será un texto, que puede o no contener paréntesis (), corchetes [] y llaves {}, además de cualquier
otra letra o símbolo. 
Su tarea es determinar que el texto sea válido, lo cual en este caso quiere decir que la utilización de paréntesis, 
corchetes y llaves es correcta, cada símbolo de apertura se corresponde con uno de cierre. 
Imprimir True o False si el texto es válido o no.

Tips:

Investigar el comportamiento de Pilas LIFO ya que son de extrema utilidad en este problema. 
Pueden utilizar listas de Python con los comandos append y pop para que se comporte como una pila LIFO.
Sugerimos usar una estructura de datos para determinar las parejas de símbolos, el código será más sencillo 
y además será mucho más fácil agregar otras parejas de símbolos en el futuro. 
Algunas opciones posibles que se nos ocurrieron, aunque no las únicas, son:
openers = ['(', '{', '[']
closers = [')', '}', ']']
brackets = {'(':')', '[':']', '{':'}'}
Ejemplos:

Cada paréntesis se cierra:

esBalanceado( "Yo (Juan) quiero (necesito) café." ) => True
Cada símbolo se cierra en el orden correcto:

esBalanceado( " { 1-[ 2*( 3+4 ) ] } " ) => True
Cada símbolo se cierra en el orden correcto:

esBalanceado( " [ [1,2,3], [4,5,6], [7,8,9] ] " ) => True
Falta cerrar el corchete ]:

esBalanceado( " [1*(2+3) " ) => False
Falta abrir la llave {:

esBalanceado( " }[]() " ) => False
Se cierran en el orden incorrecto, hay un ] entre los ( ):

esBalanceado( " { [ ( ] ) } " ) => False
'''

texto =  " { [ ( ] ) } " 
caracteres = list(texto)
brackets = {'(':')', '[':']', '{':'}', '"':'"'}
openers = list(brackets.keys())
closers = list(brackets.values())
simbolos = []

for i in caracteres:
  if i in openers or i in closers:
    simbolos.append(i)

stck = []
err = []

for i in simbolos:
  if i in openers: 
      stck.append(i) 
  elif i in closers:
    if stck != []:
      stck.pop()
    else:
      err.append("!")
if err == [] and stck == []:
  print(True)
else:
  print(False)