# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# ----
from Functions.get_Cp_debye import getOptimizedDebyeParams,get_Cp_debye
from FunctionsLayer2.get_demons import get_demons

InFolder='./INPUTS/'
filename='inputs_cleaned.csv'


df = pd.read_csv(InFolder+filename)

Temps=df.values[:, 0]
Cp=df.values[:, 1]


# bounds=[T_D_min, n_min, T_D_max, n_max]
bounds=[100, 2, 2000, 5]
params, pcov = getOptimizedDebyeParams(Temps, Cp, *bounds)

#----------------------
#test_temps = [t*10 +1 for t in range(100)]
#plt.plot(test_temps, get_Cp_debye(test_temps, *params), '--', label='fitted')
#plt.plot(Temps, Cp, 'o', label='experiment')
#----------------------


# get the demon number
temps = [t*10 +1 for t in range(100)]
demons  , weight_floor, weight_ceil =get_demons(Temps, Cp,  temps, *bounds)


#----------------------
plt.plot(demons[:, 0],demons[:, 1:4],  '--', label='demons')
#----------------------


### 
OutFolder='./OUTPUTS/'