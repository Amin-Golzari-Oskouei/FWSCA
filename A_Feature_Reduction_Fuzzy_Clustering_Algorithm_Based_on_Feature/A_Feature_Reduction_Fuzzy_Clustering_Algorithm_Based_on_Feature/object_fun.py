def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data, z, delta):
    import numpy as np

    distance = np.zeros([row, col])
    dNK = np.zeros([row, k])
    for j in range(k):
        distance = (data-np.tile(center_points[j, :], (row, 1))) ** 2
        WBETA = z * delta
        WBETA[np.where(np.isinf(WBETA))] = 0
        dNK[:, j] = np.sum(distance * WBETA, 1)
    
    WBETA = z
    WBETA[np.where(np.isinf(WBETA))] = 0 
    j_fun1 = np.sum(np.sum(dNK * np.transpose(Cluster_elem ** fuzzy_degree)))
    j_fun2 = (row/k) * np.nansum(z * np.log2(delta * z))
    j_fun  = j_fun1 + j_fun2
    return j_fun
