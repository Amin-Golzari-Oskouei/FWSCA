def object_fun(row, col, k, Cluster_elem, Cluster_elem_star, center_points, fuzzy_degree, data, z, q, sigma, pi):
    import math
    import numpy as np
    
    
    dNK = np.zeros([row, k])
    distance = np.zeros([k, row, col])
    mf = (Cluster_elem ** fuzzy_degree) + (Cluster_elem_star ** fuzzy_degree)
    
    for j in range(k):
        distance[j, :, :] = 1 - np.exp(((-1) * ((data - np.tile(center_points[j, :], (row, 1))) ** 2)) / ((2 * (sigma ** 2))))
        WBETA = np.transpose(z[j, :] ** q)
        WBETA[np.where(np.isinf(WBETA))] = 0
        dNK[:, j] = np.squeeze(np.matmul(np.reshape(distance[j, :, :], (row, col)), np.expand_dims(WBETA, 1)))
        
    j_fun1 = np.sum(np.sum(dNK * np.transpose(mf)))
    value = np.transpose(pi) * np.tile((np.exp(1 - ((1/row) * np.sum(pi, 1)))), (row, 1))
    j_fun2 = (1/row) * np.sum(np.sum(value))
    return j_fun1+j_fun2
