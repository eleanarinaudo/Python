#*-* coding: utf-8 *-*
'''
Mini desafío 3
Obtener el promedio general de todos los aprobados en Matematica.
'''



aprobMatematica=datos[(datos['Matematica']>=6)]
promedio= (aprobMatematica["Quimica"]+aprobMatematica["Fisica"]+aprobMatematica["Matematica"])/3

promedioGral= sum(promedio)/len(promedio)


print("El promedio general es %0.2f " % promedio_general)