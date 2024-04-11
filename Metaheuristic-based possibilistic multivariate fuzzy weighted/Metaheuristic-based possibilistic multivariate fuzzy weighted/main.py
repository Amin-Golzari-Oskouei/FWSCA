def main(data, center_points, k, t_max, row, fuzzy_degree, col, T_pow, a_coefficient, b_coefficient, balance_tarm):
    import numpy as np
    import math
    import sys
    from object_fun import object_fun

# -----------------------------------------------------------------------------------------

# Weights are uniformly initialized.
    z = np.ones([k, col, row])

    # Other initializations.
    Iter = 1                  # Number of iterations.
    E_w_old = math.inf        # Previous iteration objective (used to check convergence).

    Cluster_elem = np.zeros([k, col, row])
    distance = np.zeros([k, col, row])
    dwkmn= np.zeros([k, col, row])
    # --------------------------------------------------------------------------
    print('Start of proposed algorithm iterations')
    print('----------------------------------')

    # the algorithm iteration procedure
    while 1:

        # Update the cluster assignments.
        for j in range(k):
            distance[j, :, :] = np.transpose(data-np.tile(center_points[j, :], (row, 1))) ** 2
            
        distance += 10**6
        
        tmp1 = (distance ** (1/(fuzzy_degree-1))) * ((1/z) ** (fuzzy_degree / (fuzzy_degree-1)))      
        tmp2 = ((1/distance) ** (1/(fuzzy_degree-1))) * (z ** (fuzzy_degree / (fuzzy_degree-1)))  
        Cluster_elem = (tmp1 * (np.nansum(np.nansum(tmp2,1),0))) ** -1
        
        
        # Update the delta.
        delta = balance_tarm * np.sum(np.sum(distance * ((Cluster_elem/z)**fuzzy_degree),1),1) / np.sum(np.sum((Cluster_elem/z)**fuzzy_degree,1),1)
                
        # Update the T.
        dNK = np.transpose(np.sum(distance, 1))
        # Update the T.
        T = (1+((np.tile(b_coefficient/(delta*col), (row,1)) * dNK)**(1/(T_pow-1))))**-1;

               
        # Calculate the MinMax k-means objective.
        E_w = object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, z, data, T_pow, a_coefficient, b_coefficient, balance_tarm, T, delta)
        
        if math.isnan(E_w) == False:
            print(f'The algorithm objective is E_w={E_w}')

        # Check for convergence. Never converge if in the current (or previous)
        # iteration empty or singleton clusters were detected.
        if (math.isnan(E_w) == False) and (math.isnan(E_w_old) == False) and (abs(1 - E_w / E_w_old) < 10**-6 or Iter >= t_max):

            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(f'Converging for after {Iter} iterations.')
            print(f'The proposed algorithm objective is E_w={E_w}.')

            return np.nansum(Cluster_elem*z,1)

        E_w_old = E_w

        # Update the cluster centers.
        mf = (a_coefficient*((Cluster_elem/z)**fuzzy_degree)) + np.transpose(np.tile((b_coefficient*(T**T_pow)), (col,1,1)) , (2,0,1))

        for j in range(k):
            center_points[j, :] = np.nansum(np.transpose(data) * mf[j, :,:],1) / np.nansum(mf[j,:, :],1)

         
        # # # Update the feature weights.
        for j in range(k):
            distance[j, :, :] = np.transpose(data-np.tile(center_points[j, :], (row, 1))) ** 2
            
        distance += 10**6

        dwkmn = (((Cluster_elem ** fuzzy_degree) * distance) ** (1 / (fuzzy_degree+1))) 
        z = dwkmn / (np.nansum(np.nansum((dwkmn * Cluster_elem),1),0))

        Iter = Iter + 1