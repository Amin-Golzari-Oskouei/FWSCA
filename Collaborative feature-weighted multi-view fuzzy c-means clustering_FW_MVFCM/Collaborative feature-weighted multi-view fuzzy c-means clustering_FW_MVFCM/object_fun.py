def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data, z, number_viwe, w, beta):
    import math
    import numpy as np
    
    j_fun = np.zeros([number_viwe])
    
    for i in range(number_viwe):
        col = data[i].shape[1]
        distance = np.zeros([k, row, col])
        dNK = np.zeros([row, k])
        for j in range(k):
            distance = (data[i]-np.tile(center_points[i][j, :], (row, 1))) ** 2
            WBETA = z[i]**2
            WBETA[np.where(np.isinf(WBETA))] = 0
            dNK[:, j] = np.sum(w[i]**beta * distance * WBETA, 1)
        
        j_fun[i] = np.sum(np.sum(dNK * np.transpose(Cluster_elem[i] ** fuzzy_degree)))
    
    return np.sum(j_fun)
