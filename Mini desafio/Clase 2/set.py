#-*- coding: utf-8 -*-
'''
Mini-desafío: Sets
Se cuentan con varios sets que contienen las personas que les gusta un cierto sabor de helado:

vainilla = { "Juan", "Marina", "Tomas", "Paula" }
chocolate = { "Pedro", "Paula", "Marina" }
dulceDeLeche = { "Juan", "Julian", "Pedro", "Marina" }
Responder usando operaciones de sets:

Hay alguna persona que le gusten todos los gustos?

Hay alguna persona que le gusten la vainilla y no el dulce de leche?

Cuantas personas distintas tenemos?

'''


print=("Las personas que le gusta todos los sabores:", vainilla & chocolate & dulceDeLeche)
print=("Lxs personas que le gusta vainilla pero no chocolate", vainilla-chocolate)

print=(Total de personas distintas:",len(vainilla | chocolate | dulceDeLeche) )
