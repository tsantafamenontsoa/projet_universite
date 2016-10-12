# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:20:09 2016

@author: herilalaina
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

A = np.random.randn(100000) * math.sqrt(225) + 100

# Moyenne
moyenne = 0
for i in A:
    moyenne = moyenne + i
moyenne = moyenne / len(A)

# Variance
variance = 0
for i in A:
    variance = variance + (i - moyenne)**2
variance = variance / (len(A) - 1)

ecartType = math.sqrt(variance)

# Densité de probabilité
def f(x, moyenne, ecartType): 
    return (1/(ecartType*math.sqrt(2*math.pi)))*math.exp(-0.5*((x - moyenne)/ecartType)**2)

#A = np.sort(A)
f = np.vectorize(f)
Y = f(A, moyenne, ecartType)

plt.plot(A, Y, 'o')
plt.show()

# Fonction de repartition
#plt.plot(Y, np.cumsum(A), 'o')
#plt.show()

j =0
rg = np.arange(0.2, 200, 0.2)
B = np.array([])
for k in rg:
    B = np.append(B, float(len(A[A <= k])) / float(len(A)))
    j = j + 1
plt.plot(rg, B, 'o')
plt.show()
# QI superieur à 130
q130 = float(len(A[A >= 130])) / float(len(A))
q60 = float(len(A[A <= 60])) / float(len(A))

# les bornes 95% soit 2.5% pour les bornes inf et sup
borneInf = len(B[B <= 0.025])
borneSup = len(B[B <= 0.975])

valInf = rg[borneInf]
valSup = rg[borneSup]

# Partie B
A_c_r = (A - moyenne) / ecartType

# moyenne
moyenneR = 0
for i in A_c_r:
    moyenneR = moyenneR + i
moyenneR = moyenneR / len(A_c_r)

# Variance
varianceR = 0
for i in A_c_r:
    varianceR = varianceR + (i - moyenneR)**2
varianceR = varianceR / (len(A_c_r) - 1)

ecartTypeR = math.sqrt(varianceR)

#Densite & fct repartition
YR = f(A_c_r, moyenneR, ecartTypeR)

plt.plot(A_c_r, YR, 'o')
plt.show()



j =0
rg = np.arange(-4, 4, 0.02)
BR = np.array([])
for k in rg:
    BR = np.append(BR, float(len(A_c_r[A_c_r <= k])) / float(len(A_c_r)))
    j = j + 1
plt.plot(rg, BR, 'o')

q120_125 = (float(len(A[A >= 120])) +  float(len(A[A <= 125]))) / float(len(A))

q120_125R = (float(len(A_c_r[A_c_r >= ((120 - moyenne)/ecartType)])) +  float(len(A_c_r[A_c_r <= ((125 - moyenne)/ecartType)]))) / float(len(A_c_r))
