#-*- coding: utf-8 -*- 
"""### # Mini-desafio if
1. Realizar un programa que revise si una nota está aprobada (es decir si es mayor o igual a 4) utilizando un if/else. La nota será ingresada por el usuario usando input()."""

nota=int(input("Ingrese la nota: "))

if nota>=4: 
  print("Nota Aprobada")
else:  
  print("Nota Desaprobada")

"""
2. Realizar un programa que convierta una nota porcentual del 0 al 100 a una letra entre A y F de acuerdo a la siguiente conversión:

 - A: 90–100

 - B: 80–89

 - C: 70–79

 - D: 60–69

 - F: 0–59
"""
nota=int(input("Ingrese la nota porcentual entre 0 al 100: "))

if nota>=90 and 100>=nota:
  print("A")
elif nota>=80 and nota<90:
  print("B")
elif nota>=70 and nota<80:
  print("C")
elif nota>=60 and nota<70:
  print ("D")
else:
  print("F")
