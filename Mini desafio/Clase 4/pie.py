#*-* coding:utf-8 *-*
'''
Mini desafío 3
Visualizar usando un piechart la cuota de mercado de diferentes compañías que ofrecen un producto
 (por ejemplo: marcas de celulares).
Averiguar el color favorito de caramelos Sugus de diferentes amigos o conocidos y 
visualizar la información con un gráfico piechart, mostrando los colores de cada sección 
que corresponden al color de caramelo.
'''

import matplotlib.pyplot as plt

labels= ("Apple", "Samsung", "Huawei", "Xiaomi", "Lenovo", "Otro")
sizes=[72.3, 70.4, 56.2, 32.9, 31.5, 31.4]
colors=["silver","blue","red", "orange","royalblue","green"]

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.show()

