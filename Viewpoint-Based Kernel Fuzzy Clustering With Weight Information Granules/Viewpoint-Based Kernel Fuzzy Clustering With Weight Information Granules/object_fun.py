def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data, landa, z, sigma,  beta_n):
    import numpy as np

    distance = np.zeros([row, col])
    dNK = np.zeros([row, k])
    for j in range(k):
        distance = 2 - (2 * (np.exp(1) ** (((-1) * ((data - np.tile(center_points[j, :], (row, 1))) ** 2)) / (2 * (sigma ** 2)))))
        WBETA = np.transpose(z[j, :])
        WBETA[np.where(np.isinf(WBETA))] = 0
        dNK[:, j] = np.squeeze(np.matmul(distance , np.expand_dims(WBETA,1))) 
    
    WBETA = np.transpose(z[j, :])
    WBETA[np.where(np.isinf(WBETA))] = 0 
    j_fun1 = np.sum(np.sum(np.transpose(np.tile(beta_n, (k,1))) * dNK * np.transpose(Cluster_elem ** fuzzy_degree)))
    j_fun2 = (1/landa) * np.sum(np.sum(np.matmul(np.expand_dims(WBETA,1) , np.transpose(np.log2(np.expand_dims(WBETA,1))))))
    j_fun  = j_fun1 + j_fun2
    return j_fun
