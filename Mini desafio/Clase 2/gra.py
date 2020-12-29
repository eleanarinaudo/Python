#*-* coding> utf:8 *-*
'''

'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

googlefile = pd.read_csv("GOOGLE.csv")
amazonfile = pd.read_csv("AMZN.csv")
google = googlefile.to_dict("list")
amazon = amazonfile.to_dict("list")

#print(google['Open'])
#print(amazon['Open'])

plt.figure(figsize=(16, 8))

#Empiezan con el valor del primer dia
gx = [google["Date"][0]]
gy = [google["Open"][0]]
ax = [amazon["Date"][0]]
ay = [amazon["Open"][0]]

crucex = []
crucey = []

for i in range(1, len(google["Date"])): #range empieza desde 1 en vez de 0
  gx.append(google["Date"][i])
  gy.append(google["Open"][i])
  ax.append(amazon["Date"][i])
  ay.append(amazon["Open"][i])

  # Condicional de cruce (son iguales o invirtieron su orden)
  if (ay[i] == gy[i]) or (ay[i] > gy[i] and ay[i-1] < gy[i-1]) or (ay[i] < gy[i] and ay[i-1] > gy[i-1]):
    crucex.append(gx[i])
    crucey.append(gy[i])

plt.plot(gx,gy)
plt.plot(ax,ay)
plt.plot(crucex,crucey, 'k.')
plt.xticks(gx[::100], rotation=60)

plt.show()