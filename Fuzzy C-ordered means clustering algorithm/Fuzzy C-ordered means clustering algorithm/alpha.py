import numpy as np
import sys


def alpha(pi, pk, pm, pa, row, fun = 'PLOWA'):
    
    if fun == 'PLOWA':
        ans = (((pk * row) - pi) / (2 * pm  * row)) + 0.5
        ansmin = np.min([ans,1])
        return np.max([ansmin, 0])
        
    elif fun == 'SOWA':
        return 1 / ( 1 + (np.exp((2.944/(pa * row)) * (pi - (pk * row)))))
    
    else:
        print("Error!, func_name is not valid")
        sys.exit()