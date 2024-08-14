def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data, T_pow, a_coefficient, b_coefficient, balance_tarm, T, delta):
    import math
    import numpy as np

    distance = np.zeros([k, row, col])
    dNK = np.zeros([row, k])
    mf  = (a_coefficient*np.transpose(Cluster_elem**fuzzy_degree)) + (b_coefficient*(T**T_pow))
    
    
    for j in range(k):
        distance = (data-np.tile(center_points[j, :], (row, 1))) ** 2
        dNK[:, j] = np.sqrt(np.sum(distance, 1))
        
    j_fun1 = np.sum(np.sum(dNK * mf, 0))
    
    j_fun2 = np.sum(np.sum((1-T)**T_pow,0) * delta);
    
    return j_fun1 + j_fun2
