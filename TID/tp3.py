# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:23:26 2016

@author: tsanta
"""
import numpy as np

data = [95, 109, 99, 83, 113, 86, 101, 92, 96, 106]


# Methode de bootstrap
mean_bootstrap = np.array([])
for i in range (0, 1000):
    data_bootstrap = np.array([])    
    for j in range(0, 10):
        k = np.random.randint(0, len(data))
        data_bootstrap = np.append(data[k], data_bootstrap)
    mean_bootstrap = np.append(np.mean(data_bootstrap), mean_bootstrap)    
    
mean_bootstrap_sorted = np.sort(mean_bootstrap)
mean_bootstrap_95 = mean_bootstrap_sorted[25:975]

print("La moyenne de l'echantillon est {0}".format(np.mean(data)))
print("Le minimum de la moyenne de bootstrap est {0}".format(mean_bootstrap_95.min()))
print("Le maximum de la moyenne de bootstrap est {0}".format(mean_bootstrap_95.max()))

#import cPickle as pkl
#Y = pkl.load("")