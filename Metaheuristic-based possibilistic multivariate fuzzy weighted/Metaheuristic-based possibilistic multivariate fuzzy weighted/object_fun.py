def object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, z, data, T_pow, a_coefficient, b_coefficient, balance_tarm, T, delta):
    import numpy as np
    distance = np.zeros([k, col, row])

    for j in range(k):
        distance[j, :, :] = np.transpose(data - np.tile(center_points[j, :], (row, 1))) ** 2

    distance += 10**6
    
    mf = (a_coefficient*((Cluster_elem/z)**fuzzy_degree)) + np.transpose(np.tile((b_coefficient*(T**T_pow)), (col,1,1)) , (2,0,1))       
    j_fun1 = np.nansum(mf * distance)  
    j_fun2 = np.sum(np.sum((1-T)**T_pow,0) * delta);
    
    
    return j_fun1 + col * j_fun2
