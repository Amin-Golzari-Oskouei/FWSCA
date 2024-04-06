def main(data, center_points, k, t_max, row, fuzzy_degree, col, T_pow, a_coefficient, b_coefficient, balance_tarm):
    import numpy as np
    import math
    import sys
    from object_fun import object_fun
    
    
    if a_coefficient < 0:
        print('Error: a coefficient must be a non-negative number', file=sys.stderr)
        sys.exit()

    if b_coefficient < 0:
        print('Error: b coefficient must be a non-negative number', file=sys.stderr)
        sys.exit()
        
    if balance_tarm < 0:
        print('Error: balance tarm coefficient must be a non-negative number', file=sys.stderr)
        sys.exit()
        
    if fuzzy_degree <= 1 :
        print('Error: fuzzy degree must be more than one', file=sys.stderr)
        sys.exit()
        
    if T_pow <= 1 :
        print('Error: T_pow must be more than one', file=sys.stderr)
        sys.exit()
        
#-----------------------------------------------------------------------------------------
    # Other initializations.
    Iter = 1                  # Number of iterations.
    E_w_old = math.inf        # Previous iteration objective (used to check convergence).

    Cluster_elem = np.zeros([k, row])
    T = np.ones([k, col]) / col
    distance = np.zeros([k, row, col])
    dNK = np.zeros([row, k])

    # --------------------------------------------------------------------------
    print('Start of Fuzzy C-Means iterations')
    print('----------------------------------')

    # the algorithm iteration procedure
    while 1:

        # Update the cluster assignments.
        for j in range(k):
            distance = (data-np.tile(center_points[j, :], (row, 1))) ** 2
            dNK[:, j] = np.sqrt(np.sum(distance, 1))

        tmp1 = np.zeros([row, k])
        for j in range(k):
            tmp2 = (dNK / np.transpose(np.tile(dNK[:, j], (k, 1)))) ** (2 / (fuzzy_degree - 1))
            tmp2[np.where(np.isnan(tmp2))] = 0
            tmp2[np.where(np.isinf(tmp2))] = 0
            tmp1 = tmp1 + tmp2

        Cluster_elem = np.transpose(1 / tmp1)
        Cluster_elem[np.where(np.isnan(Cluster_elem))] = 1
        Cluster_elem[np.where(np.isinf(Cluster_elem))] = 1

        for j in np.where(dNK == 0)[0]:
            Cluster_elem[np.where(dNK[j, :] == 0)[0], j] = 1 / len(np.where(dNK[j, :] == 0)[0])
            Cluster_elem[np.where(dNK[j, :] != 0)[0], j] = 0
            

        # Update the delta.
        delta = balance_tarm * np.sum(dNK * np.transpose(Cluster_elem**fuzzy_degree),0) / np.sum(Cluster_elem**fuzzy_degree,1)
        
        # Update the T.
        T = (1+((np.tile(b_coefficient/delta, (row,1)) * dNK)**(1/(T_pow-1))))**-1;

        # Calculate the MinMax k-means objective.
        E_w = object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data, T_pow, a_coefficient, b_coefficient, balance_tarm, T, delta)

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
        mf = np.transpose((a_coefficient*np.transpose(Cluster_elem**fuzzy_degree)) + (b_coefficient*(T**T_pow)))
        for j in range(k):
            center_points[j, :] = np.matmul(np.expand_dims(mf[j, :], 0), data) / np.matmul(np.expand_dims(mf[j, :], 0), np.ones_like(data))

        Iter = Iter + 1
