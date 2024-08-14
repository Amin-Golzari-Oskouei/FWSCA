def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, z, data):
    import numpy as np
    distance = np.zeros([k, col, row])

    for j in range(k):
        distance[j, :, :] = np.transpose(data - np.tile(center_points[j, :], (row, 1))) ** 2

    distance += 10**6
    mf = (Cluster_elem / z) ** fuzzy_degree

        
    j_fun = np.nansum(mf * distance)
    
    return j_fun
