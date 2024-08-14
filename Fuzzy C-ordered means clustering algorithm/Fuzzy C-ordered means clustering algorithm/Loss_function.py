import numpy as np
import sys


def loss_function(func_name, Enkm, delta=1, alpha=1, beta=1):
    
    if func_name == 'LINear' or func_name == 'LIN':
        if Enkm == 0:
            return 0
        else:
            return (1 / (np.abs(Enkm)))
        
    elif func_name == 'HUBer' and delta > 0:
        if np.abs(Enkm) <= delta:
            return (1 / (delta ** 2))
        else:
            return (1 / (np.abs(Enkm) * delta))
    
    elif func_name == 'SIGmoidal' or func_name == 'SIG' and alpha > 0 and beta > 0:
        if Enkm == 0:
            return 0
        else:
            return (1 / ((Enkm ** 2) * (1 + np.exp((-1 * alpha) * (np.abs(Enkm) - beta)))))
    
    elif func_name == 'SIGmoidal-Linear' or func_name == 'SIGL' and alpha > 0 and beta > 0:
        if Enkm == 0:
            return 0
        else:
            return (1 / (np.abs(Enkm) * (1 + np.exp((-1 * alpha) * (np.abs(Enkm) - beta)))))
    
    elif func_name == 'LOGarithmic' or func_name == 'LOG':
        if Enkm == 0:
            return 0
        else:
            return ((np.log10(1 + (Enkm ** 2))) / (Enkm ** 2))
    
    elif func_name == 'LOG-Linear' or func_name == 'LOGL':
         if Enkm == 0:
            return 0
         else:
            return ((np.log10(1 + (Enkm ** 2))) / (np.abs(Enkm)))
        
    elif func_name == 'Essential' or func_name == 'ESS':
         if Enkm == 0:
            return 0
         else:
            return 1
    
    else:
        print("Error!, func_name is not valid")
        sys.exit()