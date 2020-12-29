"""Mini-desafio
Realizar un programa al cual se ingresa el dia del anio mediante un numero de 0 a 364, y que muestra en pantalla a que dia de la semana corresponde mediante un numero de 0 a 6 (mostrar el numero 0 si corresponde a Lunes y 6 si es Domingo)

Suponemos que el dia 0 del año cae un Lunes.

Pista (seleccionar texto para ver): Los dias multiplos de 7 corresponden a 0 (Lunes), los dias que tienen resto 1 en la division por 7 corresponden a 1 (Martes), los dias que tienen resto 2 en la division por 7 corresponden a 2 (Miercoles), etc."""


dia=int(input("Ingrese el dia del año de 0 a 354: "))
print (dia%7)