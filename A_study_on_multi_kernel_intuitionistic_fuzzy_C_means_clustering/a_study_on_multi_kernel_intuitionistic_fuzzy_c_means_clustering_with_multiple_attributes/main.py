def main(data, center_points, k, t_max, row, fuzzy_degree, col, q, sigma, beta):
    import numpy as np
    import math
    import sys
    from object_fun import object_fun
    
    if q <= 1:
        print('Error: q must be a more than 1', file=sys.stderr)
        sys.exit()
    
    if beta <= 0:
        print('Error: beta must be a postive value', file=sys.stderr)
        sys.exit()
        
#-----------------------------------------------------------------------------------------
    # Other initializations.
    Iter = 1                  # Number of iterations.
    E_w_old = math.inf        # Previous iteration objective (used to check convergence).


    # Weights are uniformly initialized.
    z = np.ones([k, col]) / col

    # Other initializations.
    Cluster_elem = np.zeros([k, row])
    Cluster_elem_star = np.zeros([k, row])
    distance = np.zeros([k, row, col])
    dNK = np.zeros([row, k])
    dwkm= np.zeros([k, col])
    dwm= np.zeros([col])
    pi = np.zeros([k, row])
    # --------------------------------------------------------------------------
    
    print('Start of Fuzzy C-Means iterations')
    print('----------------------------------')

    # the algorithm iteration procedure
    while 1:

        # Update the cluster assignments.
        for j in range(k):
            distance[j, :, :] = 1 - np.exp(((-1) * ((data - np.tile(center_points[j, :], (row, 1))) ** 2)) / ((2 * (sigma ** 2))))
            WBETA = np.transpose(z[j, :] ** q)
            WBETA[np.where(np.isinf(WBETA))] = 0
            dNK[:, j] = np.squeeze(np.matmul(np.reshape(distance[j, :, :], (row, col)), np.expand_dims(WBETA, 1)))

        tmp1 = np.zeros([row, k])
        for j in range(k):
            tmp2 = (dNK / np.transpose(np.tile(dNK[:, j], (k, 1)))) ** (1 / (fuzzy_degree - 1))
            tmp2[np.where(np.isnan(tmp2))] = 0
            tmp2[np.where(np.isinf(tmp2))] = 0
            tmp1 = tmp1 + tmp2

        Cluster_elem = np.transpose(1 / tmp1)
        Cluster_elem[np.where(np.isnan(Cluster_elem))] = 1
        Cluster_elem[np.where(np.isinf(Cluster_elem))] = 1

        for j in np.where(dNK == 0)[0]:
            Cluster_elem[np.where(dNK[j, :] == 0)[0], j] = 1 / len(np.where(dNK[j, :] == 0)[0])
            Cluster_elem[np.where(dNK[j, :] != 0)[0], j] = 0

        # Update Unk star
        Cluster_elem_star = 1 - ((1 - (Cluster_elem ** beta)) ** (1/beta))

        # Update pi
        pi = Cluster_elem_star - Cluster_elem

        # Calculate the MinMax k-means objective.
        E_w = object_fun(row, col, k, Cluster_elem, Cluster_elem_star, center_points, fuzzy_degree, data, z, q, sigma, pi)

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
        mf = (Cluster_elem ** fuzzy_degree) + (Cluster_elem_star ** fuzzy_degree)

        for j in range(k):
            tmp = np.exp(((-1) * ((data - np.tile(center_points[j, :], (row, 1))) ** 2)) / ((2 * (sigma ** 2))))
            center_points[j, :] = np.matmul(np.expand_dims(mf[j, :], 0), (data * tmp)) / np.matmul(np.expand_dims(mf[j, :], 0), (np.ones_like(data) * tmp))

        
        # # Update the feature weights.
        for j in range(k):
            distance[j, :, :] = 1 - np.exp(((-1) * ((data - np.tile(center_points[j, :], (row, 1))) ** 2)) / ((2 * (sigma ** 2))))
            dwkm[j, :] = np.matmul(mf[j, :], np.reshape(distance[j, :, :], (row, col)))
            

        tmp1 = np.zeros([k, col])
        for j in range(col):
            tmp2 = (dwkm / (np.tile(np.expand_dims(dwkm[:, j],1), (1, col)))) ** (1 / (q - 1))
            tmp2[np.where(np.isnan(tmp2))] = 0
            tmp2[np.where(np.isinf(tmp2))] = 0
            tmp1 = tmp1 + tmp2

        z = (1 / tmp1)
        z[np.where(np.isnan(z))] = 1
        z[np.where(np.isinf(z))] = 1

        for j in np.where(dwkm == 0)[0]:
            z[j, np.where(dwkm[j, :] == 0)[0]] = 1 / len(np.where(dwkm[j, :] == 0)[0])
            z[j, np.where(dwkm[j, :] != 0)[0]] = 0


        Iter = Iter + 1
