def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data):
    import numpy as np
    distance = np.zeros([k, col, row])

    for j in range(k):
        distance[j, :, :] = np.transpose((data-center_points[j, :]) ** 2)
        
    mf = Cluster_elem ** fuzzy_degree 
    j_fun = np.nansum(mf * distance)
    
    return j_fun
