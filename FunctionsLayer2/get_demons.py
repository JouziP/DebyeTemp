# -*- coding: utf-8 -*-

import numpy as np

from Functions.get_Cp_debye import getOptimizedDebyeParams, get_Cp_debye


def get_demons(experimental_temps, 
               experimental_Cp, 
               target_temps_range, 
               *bounds):
    #    
    k_b=1.38064852E-23
    Na=6.022E+23
    n_kinetic = 3
    #
    params, pcov = getOptimizedDebyeParams(experimental_temps,
                                           experimental_Cp, 
                                           *bounds)
    
    Cp_debye = get_Cp_debye(target_temps_range, *params)
    demon_number_floor = [ (0, np.floor((cp/(k_b*Na) - n_kinetic)) )[(cp/(k_b*Na) - n_kinetic) > 0] \
                for cp in  np.array(Cp_debye) ]
    demon_number_ceil = [ (0, np.ceil((cp/(k_b*Na) - n_kinetic)) )[(cp/(k_b*Na) - n_kinetic) > 0] \
                for cp in  np.array(Cp_debye) ]
    ### calculate floor weight: the diference between cp/(k_b*Na) - n_kinetic and floor
    weight_floor = [1 -\
                    np.sqrt(np.abs(demon_number_floor[i]-\
                                   Cp_debye[i]/(k_b*Na)+n_kinetic)**2)  \
            for i in range(len( demon_number_floor))       \
            ]
    ### calculate ceil weight: the diference between cp/(k_b*Na) - n_kinetic and ceil
    weight_ceil = [1 -\
                   np.sqrt(np.abs(demon_number_ceil[i]-\
                                   Cp_debye[i]/(k_b*Na)+n_kinetic)**2)  \
            for i in range(len( demon_number_floor))       \
            ]
    #### average of demons: demon_number_avg
    demon_number_avg = [weight_floor[i]*demon_number_floor[i] +\
                 weight_ceil[i]*demon_number_ceil[i] for i in range(len( demon_number_floor))]
    ####
    demons=np.zeros([len(target_temps_range), 4])
    demons[:, 0]= target_temps_range
    demons[:, 1]= demon_number_ceil
    demons[:, 2]= demon_number_floor
    ### the average:
    demons[:, 3]= demon_number_avg
    return demons , weight_floor, weight_ceil
