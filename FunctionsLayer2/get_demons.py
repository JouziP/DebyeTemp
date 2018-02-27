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
    pass
    ### calculate ceil weight: the diference between cp/(k_b*Na) - n_kinetic and ceil
    pass
    #### average of demons: demon_number_avg
    pass
    ####
    demons=np.zeros([len(target_temps_range), 3])
    demons[:, 0]= target_temps_range
    demons[:, 1]= demon_number_ceil
    demons[:, 2]= demon_number_floor
    ### the average:
    # demons[:, 3]= demon_number_avg
    return demons
