def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data, sigma):
    import math
    import numpy as np

    distance = np.zeros([k, row, col])
    dNK = np.zeros([row, k])
    for j in range(k):
        distance = 1-np.exp((-1*((data-np.tile(center_points[j, :], (row, 1))) ** 2)) / (2*(sigma**2)))
        dNK[:, j] = np.sum(distance, 1)
        
    j_fun = np.sum(np.sum(dNK * np.transpose(Cluster_elem ** fuzzy_degree)))
    return j_fun
