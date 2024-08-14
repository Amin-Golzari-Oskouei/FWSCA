def main(data, center_points, k, t_max, row, fuzzy_degree, col):
    import numpy as np
    import math
    import sys
    from object_fun import object_fun

# -----------------------------------------------------------------------------------------

    # Other initializations.
    Iter = 1                  # Number of iterations.
    E_w_old = math.inf        # Previous iteration objective (used to check convergence).

    Cluster_elem = np.zeros([k, col, row])
    distance = np.zeros([k, col, row])
    # --------------------------------------------------------------------------
    print('Start of proposed algorithm iterations')
    print('----------------------------------')

    # the algorithm iteration procedure
    while 1:

        # Update the cluster assignments.
        for j in range(k):
            distance[j, :, :] = np.transpose((data-center_points[j, :]) ** 2)
    
        tmp1 = (distance) ** (1 / (fuzzy_degree - 1))
        tmp2 = (distance) ** (-1 / (fuzzy_degree - 1))
        tmp2 = (np.nansum(np.nansum(tmp2, 1), 0))
        Cluster_elem = (tmp1 * tmp2) ** -1
        

        for j in np.where(distance == 0)[2]:
            Cluster_elem[np.where(distance[:, :, j] == 0)[0], np.where(distance[:, :, j] == 0)[1], j] = 1 / len(np.where(distance[:,:, j] == 0)[1])
            Cluster_elem[np.where(distance[:, :, j] != 0)[0], np.where(distance[:, :, j] != 0)[1], j] = 0
        

        # Calculate the MinMax k-means objective.
        E_w = object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data)
        
        if math.isnan(E_w) == False:
            print(f'The algorithm objective is E_w={E_w}')

        # Check for convergence. Never converge if in the current (or previous)
        # iteration empty or singleton clusters were detected.
        if (math.isnan(E_w) == False) and (math.isnan(E_w_old) == False) and (abs(E_w - E_w_old) < 10**-6 or Iter >= t_max):

            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(f'Converging for after {Iter} iterations.')
            print(f'The proposed algorithm objective is E_w={E_w}.')

            return np.nansum(Cluster_elem, 1)

        E_w_old = E_w

        # Update the cluster centers.
        mf = Cluster_elem ** fuzzy_degree

        for j in range(k):
            center_points[j, :] = np.nansum(np.transpose(data) * mf[j, :, :], 1) / np.nansum(mf[j, :, :], 1)
        
        Iter = Iter + 1