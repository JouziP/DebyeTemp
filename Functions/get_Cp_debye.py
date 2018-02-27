# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import quad





def integrant(x):
    return x**4* np.exp(x)/(np.exp(x) - 1)**2

def get_Cp_debye(Temps, Temp_debye, n):
    _zero=0.0001
    k_b=1.38064852E-23
    Na=6.022E+23
    N = n * Na
    rslt = [9*(N*k_b)*(Temp*1./Temp_debye)**3 *\
                quad(integrant, _zero , Temp_debye*1./np.array(Temp))[0]\
                for Temp in Temps ]
    
    return rslt

#
#
def getOptimizedDebyeParams(Temps_experimental, 
                            Cp_experimental, 
                            T_D_min=0,
                            n_min=0,
                            T_D_max=1000,
                            n_max=6):
    #
    param, pcov= curve_fit(get_Cp_debye, 
                           Temps_experimental, 
                           Cp_experimental, 
                           bounds=[[T_D_min,n_min], [T_D_max, n_max]]
                           )
    return param, pcov








