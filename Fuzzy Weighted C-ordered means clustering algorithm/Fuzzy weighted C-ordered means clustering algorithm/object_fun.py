def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, z, q, data, beta):
    import math
    import numpy as np
    
    
    dNK = np.zeros([row, k])
    distance = np.zeros([k, row, col])
    mf = np.transpose(Cluster_elem ** fuzzy_degree)
    
    for j in range(k):
        distance[j, :, :] = (data - np.tile(center_points[j, :], (row, 1))) ** 2
        WBETA = np.transpose(z[j, :] ** q)
        WBETA[np.where(np.isinf(WBETA))] = 0
        dNK[:, j] = np.squeeze(np.matmul(np.reshape(distance[j, :, :], (row, col)), np.expand_dims(WBETA, 1)))
        
    j_fun1 = np.sum(np.sum(dNK * mf * np.transpose(beta)))

    return j_fun1
