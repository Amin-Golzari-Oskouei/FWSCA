def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data, z, simga, q):
    import math
    import numpy as np
    
    
    dNK = np.zeros([row, k])
    for j in range(k):
        distance = 1-np.exp((-1*((data-np.tile(center_points[j, :], (row, 1))) ** 2)) / (2*(simga**2)))
        WBETA = z**q
        WBETA[np.where(np.isinf(WBETA))] = 0
        dNK[:, j] = np.sum(distance * WBETA, 1)
        
    j_fun = np.sum(np.sum(dNK * np.transpose(Cluster_elem ** fuzzy_degree)))
    
    return j_fun
