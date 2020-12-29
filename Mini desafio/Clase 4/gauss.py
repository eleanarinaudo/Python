#*-* coding:utf-8 *-*
'''
### Mini desafío 1

Gráficar en el intervalo de **[-5, 5]** una [función gaussiana]
 definida como:

$$ f(x) = e^{-x^2/2} $$

Usar la funcion [np.exp](https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html) de numpy.
'''

import matplotlib.pyplot as plt
import numpy as np
import math 


X = np.linspace(-5, 5,100000)
gaussiana= np.exp(-X**2/2)


plt.plot(X, gaussiana)
plt.show()