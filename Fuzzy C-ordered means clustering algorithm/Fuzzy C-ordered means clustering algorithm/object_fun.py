def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data, beta, loss_type):
    import math
    import numpy as np
    from Loss_function import loss_function
    
    
    dNK = np.zeros([row, k])
    distance = np.zeros([k, row, col])
    mf = np.transpose(Cluster_elem ** fuzzy_degree)
    
    vfunc = np.vectorize(loss_function)
    for j in range(k):
        distance = vfunc (loss_type, np.abs(data - np.tile(center_points[j, :], (row, 1))) ** 2)
        dNK[:, j] = np.sum(distance, 1)
        
    j_fun1 = np.sum(np.sum(dNK * mf * np.transpose(beta)))

    return j_fun1
