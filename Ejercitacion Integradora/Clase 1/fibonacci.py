#-*- coding: UTF-8 *-*
"""La leyenda de Filius Bonacci"""
a0=0
a1=1

for i in range(10):
    if i%2==0:
        print(a0)
        a0+=a1
    else:
        print(a1)
        a1+=a0