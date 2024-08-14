def main(data, center_points, k, t_max, row, fuzzy_degree, col):
    import numpy as np
    import math
    import sys
    from object_fun import object_fun

        
#-----------------------------------------------------------------------------------------
    # Other initializations.
    Iter = 1                  # Number of iterations.
    E_w_old = math.inf        # Previous iteration objective (used to check convergence).


    # Weights are uniformly initialized.
    z = np.ones([col]) / col
    delta = (np.sum(data, 0) / row) / np.var(data, 0)
    landa = np.var(data) / ((fuzzy_degree ** 2) * k)
    # Other initializations.
    Cluster_elem = np.zeros([k, row])
    distance = np.zeros([k, row, col])
    dNK = np.zeros([row, k])
    dwkm= np.zeros([k, col])
    dwm = np.zeros([col])
    # --------------------------------------------------------------------------
    
    print('Start of Fuzzy C-Means iterations')
    print('----------------------------------')

    # the algorithm iteration procedure
    while 1:

        # Update the cluster assignments.
        for j in range(k):
            distance = (data-np.tile(center_points[j, :], (row, 1))) ** 2
            WBETA = z * delta
            WBETA[np.where(np.isinf(WBETA))] = 0
            dNK[:, j] = np.sum(distance * WBETA, 1)

        
        Cluster_elem = (1 + (((landa ** -1) * np.transpose(dNK)) ** (1/(fuzzy_degree - 1)))) ** -1

        # Calculate the MinMax k-means objective.
        E_w = object_fun(landa, row, col, k, Cluster_elem, center_points, fuzzy_degree, data , z, delta)

        if math.isnan(E_w) == False:
            print(f'The algorithm objective is E_w={E_w}')

        # Check for convergence. Never converge if in the current (or previous)
        # iteration empty or singleton clusters were detected.
        if (math.isnan(E_w) == False) and (math.isnan(E_w_old) == False) and (abs(1 - E_w / E_w_old) < 10**-6 or Iter >= t_max):

            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(f'Converging for after {Iter} iterations.')
            print(f'The proposed algorithm objective is E_w={E_w}.')

            return Cluster_elem

        E_w_old = E_w

        # Update the cluster centers.
        mf = Cluster_elem ** fuzzy_degree
        for j in range(k):
            center_points[j, :] = np.matmul(np.expand_dims(mf[j, :], 0), data) / np.matmul(np.expand_dims(mf[j, :], 0), np.ones_like(data))

        
        # # Update the feature weights.
        for j in range(k):
            distance = ((data-np.tile(center_points[j, :], (row, 1))) ** 2) * delta
            dwkm[j, :] = np.matmul(Cluster_elem[j, :] ** fuzzy_degree, distance) + landa * np.sum((1-Cluster_elem[j, :])** fuzzy_degree)
            
        dwm = ((1/delta) * np.exp((-1*k/row) * np.sum(dwkm, 0))) ** -1

        tmp1 = np.zeros([col])
        for j in range(col):
            tmp2 = (dwm / (np.tile(dwm[j], (1, col))))
            tmp2[np.where(np.isnan(tmp2))] = 0
            tmp2[np.where(np.isinf(tmp2))] = 0
            tmp1 = tmp1 + tmp2

        z = (1 / tmp1)
        z[np.where(np.isnan(z))] = 1
        z[np.where(np.isinf(z))] = 1

        for j in np.where(dwm == 0)[0]:
            z[j, np.where(dwm[j, :] == 0)[0]] = 1 / len(np.where(dwm[j, :] == 0)[0])
            z[j, np.where(dwm[j, :] != 0)[0]] = 0

        # check threshold
        threshold = 1 / (np.sqrt(row * col * k))     
        z[z <= threshold] = 0
        
        # normalize 
        z = z / np.sum(z)

        Iter = Iter + 1
