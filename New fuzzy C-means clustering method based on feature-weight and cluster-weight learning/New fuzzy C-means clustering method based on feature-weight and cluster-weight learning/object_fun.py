def object_fun(row, col, k, Cluster_elem, landa, center_points, fuzzy_degree, w, z, q, p, data):
    import math
    import numpy as np
    distance = np.zeros([k, row, col])
    dNK = np.zeros([row, k])
    for j in range(k):
        distance[j, :, :] = (1 - np.exp((-1 * np.tile(landa, (row, 1))) * ((data - np.tile(center_points[j, :], (row, 1))) ** 2)))
        WBETA = np.transpose(z[j, :] ** q)
        WBETA[np.where(np.isinf(WBETA))] = 0
        dNK[:, j] = np.squeeze(np.matmul(w[j] ** p * np.reshape(distance[j, :, :], (row, col)), np.expand_dims(WBETA, 1)))
    j_fun = np.sum(np.sum(dNK * np.transpose(Cluster_elem ** fuzzy_degree)))
    return j_fun
