def main(data, center_points, k, p_init, p_max, p_step, t_max, beta_memory, row, fuzzy_degree, col, q, landa):
    import numpy as np
    import math
    import sys
    from object_fun import object_fun
    if p_init < 0 or p_init >= 1:
        print('Error: p_init must take a value in [0,1)', file=sys.stderr)
        sys.exit()

    if p_max < 0 or p_max >= 1:
        print('Error: p_max must take a value in [0,1)', file=sys.stderr)
        sys.exit()

    if p_max < p_init:
        print('Error: p_max must be greater or equal to p_init', file=sys.stderr)
        sys.exit()

    if p_step < 0:
        print('Error: p_step must be a non-negative number', file=sys.stderr)
        sys.exit()

    if beta_memory < 0 or beta_memory > 1:
        print('Error: beta_memory must take a value in [0,1]', file=sys.stderr)
        sys.exit()

    if q == 0:
        print('Error: q must be a non-zero number', file=sys.stderr)
        sys.exit()

    if p_init == p_max:
        if p_step != 0:
            print('p_step reset to zero, since p_max equals p_init')
        p_flag = 0
        p_step = 0
    elif p_step == 0:
        if p_init != p_max:
            print('p_max reset to equal p_init, since p_step=0')
        p_flag = 0
        p_max = p_init
    else:
        p_flag = 1  # p_flag indicates whether p will be increased during the iterations.

# -----------------------------------------------------------------------------------------

# Weights are uniformly initialized.
    w = np.ones(k)/k
    z = np.ones([k, col]) / col

    # Other initializations.
    p = p_init                # Initial p value.
    p_prev = p - 10 ** (-8)   # Dummy value.
    empty = 0                 # Count the number of iterations for which an empty or singleton cluster is detected.
    Iter = 1                  # Number of iterations.
    E_w_old = math.inf        # Previous iteration objective (used to check convergence).

    Cluster_elem = np.zeros([k, row])
    Cluster_elem_history = np.zeros([k, row])
    w_history = np.zeros(k)
    distance = np.zeros([k, row, col])
    z_history = np.zeros([k, col])
    dNK = np.zeros([row, k])
    dwkm= np.zeros([k, col])
    dw = np.zeros([k])

    # --------------------------------------------------------------------------
    print('Start of proposed algorithm iterations')
    print('----------------------------------')

    # the algorithm iteration procedure
    while 1:

        # Update the cluster assignments.
        for j in range(k):
            distance[j, :, :] = (1-np.exp((-1 * np.tile(landa, (row, 1))) * ((data-np.tile(center_points[j, :], (row, 1))) ** 2)))
            WBETA = np.transpose(z[j, :] ** q)
            WBETA[np.where(np.isinf(WBETA))] = 0
            dNK[:, j] = np.squeeze(np.matmul( w[j] ** p * np.reshape(distance[j, :, :], (row, col)), np.expand_dims(WBETA, 1)))

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

        # Calculate the MinMax k-means objective.
        E_w = object_fun(row, col, k, Cluster_elem, landa, center_points, fuzzy_degree, w, z, q, p, data)

        # If empty or singleton clusters are detected after the update.
        for i in range(k):
            I = np.count_nonzero((Cluster_elem[i, :] <= 0.05))

            if I == row-1 or I == row:
                print(f'Empty or singleton clusters detected for p={p}.')
                print('Reverting to previous p value.')

                math.isnan(E_w)
                empty = empty + 1

                if empty > 1:
                    p = p - p_step
                    # The last p increase may not correspond to a complete p_step,
                    # if the difference p_max-p_init is not an exact multiple of p_step.
                else:
                    p = p_prev

                p_flag = 0  # Never increase p again.

                # p is not allowed to drop out of the given range.
                if p < p_init or p_step == 0:
                    print('+++++++++++++++++++++++++++++++++++++++++')
                    print('p cannot be decreased further.')
                    print('Either p_step=0 or p_init already reached.')
                    print('Aborting Execution')
                    print('+++++++++++++++++++++++++++++++++++++++++')

                    # Return NaN to indicate that no solution is produced
                    center_points[:, :] = np.nan
                    return

                # Continue from the assignments and the weights corresponding
                # to the decreased p value.
                a = (k * empty) - (k - 1) - 1
                b = k * empty
                Cluster_elem = Cluster_elem_history[a:b, :]
                w = w_history[a:b]
                z = z_history[a:b, :]
                break

        if math.isnan(E_w) == False:
            print(f'p={p}')
            print(f'The algorithm objective is E_w={E_w}')

        # Check for convergence. Never converge if in the current (or previous)
        # iteration empty or singleton clusters were detected.
        if (math.isnan(E_w) == False) and (math.isnan(E_w_old) == False) and (abs(1 - E_w / E_w_old) < 10**-6 or Iter >= t_max):

            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(f'Converging for p={p} after {Iter} iterations.')
            print(f'The proposed algorithm objective is E_w={E_w}.')

            return Cluster_elem

        E_w_old = E_w

        # Update the cluster centers.
        mf = Cluster_elem ** fuzzy_degree
        for j in range(k):
            center_points[j, :] = np.matmul(np.expand_dims(mf[j, :], 0), (data * (np.exp((-1 * np.tile(landa, (row, 1))) * ((data-np.tile(center_points[j, :], (row, 1))) ** 2))))) / np.matmul(np.expand_dims(mf[j, :], 0), ((np.exp((-1 * np.tile(landa, (row, 1))) * ((data-np.tile(center_points[j, :], (row, 1))) ** 2)))))


        # Increase the p value.
        if p_flag == 1:
            # Keep the assignments-weights corresponding to the current p.
            # These are needed when empty or singleton clusters are found in subsequent iterations.
            Cluster_elem_history = np.concatenate((Cluster_elem, Cluster_elem_history), axis=0)
            w_history = np.concatenate((w, w_history), axis=0)
            z_history = np.concatenate((z, z_history), axis=0)

            p_prev = p
            p = p + p_step

            if p >= p_max:
                p = p_max
                p_flag = 0
                print('p_max reached')

        w_old = w
        z_old = z
        #
        # # Update the feature weights.
        for j in range(k):
            distance[j, :, :] = (1 - np.exp((-1 * np.tile(landa, (row, 1))) * ((data - np.tile(center_points[j, :], (row, 1))) ** 2)))
            dwkm[j, :] = np.matmul(Cluster_elem[j, :] ** fuzzy_degree, np.reshape(distance[j, :, :], (row, col)))

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

        # # Update the cluster weights.
        for j in range(k):
            distance[j, :, :] = (1 - np.exp((-1 * np.tile(landa, (row, 1))) * ((data - np.tile(center_points[j, :], (row, 1))) ** 2)))
            WBETA = np.transpose(z[j, :] ** q)
            WBETA[np.where(np.isinf(WBETA))] = 0
            dw[j] = np.matmul(np.matmul(np.transpose(WBETA), np.transpose(np.reshape(distance[j, :, :], (row, col)))), np.transpose(Cluster_elem[j, :] ** fuzzy_degree))

        tmp = np.sum((np.tile(dw, (k, 1)) / np.transpose(np.tile(dw, (k, 1)))) ** (1/(p-1)), axis=0)
        tmp[np.where(np.isnan(tmp))] = 0
        tmp[np.where(np.isinf(tmp))] = 0
        w = 1/tmp
        w[np.where(np.isnan(w))] = 1
        w[np.where(np.isinf(w))] = 1

        if len(np.where(dw == 0)[0]) > 0:
            w[np.where(dw == 0)[0]] = 1 / len(np.where(dw == 0)[0])
            w[np.where(dw != 0)[0]] = 0

        # Memory effect.
        w = (1 - beta_memory) * w + beta_memory * w_old
        z = (1 - beta_memory) * z + beta_memory * z_old

        Iter = Iter + 1