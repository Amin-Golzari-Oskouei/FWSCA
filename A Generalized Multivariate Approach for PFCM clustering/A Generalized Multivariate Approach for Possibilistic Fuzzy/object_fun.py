def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, z, data, T_pow, a_coefficient, b_coefficient, balance_tarm, T, delta):
    import numpy as np
    distance = np.zeros([k, col, row])

    for j in range(k):
        distance[j, :, :] = np.transpose((data-center_points[j, :]) ** 2)
        
    
    mf = ((a_coefficient*(Cluster_elem**fuzzy_degree)) + (b_coefficient*(T**T_pow))) 
    j_fun = np.nansum(mf * (np.transpose(np.tile(z, (row,1,1)), (1, 2, 0)) * distance))
    
    j_fun2 = np.nansum(np.nansum((1-T)**T_pow,2) * (delta * z));
    
    return j_fun + j_fun2
