def main(data, center_points, k, t_max, row, fuzzy_degree, number_viwe, beta, landa):
    import numpy as np
    import math
    import sys
    from object_fun import object_fun
    
        
#-----------------------------------------------------------------------------------------
    # Other initializations.
    Iter = 1                  # Number of iterations.
    E_w_old = math.inf        # Previous iteration objective (used to check convergence).


    # Weights are uniformly initialized.
    z = {}
    for i in range(number_viwe):
        z[i] = np.ones([data[i].shape[1]]) / data[i].shape[1]
        
    
    # Weights are uniformly initialized.
    w = np.ones([number_viwe]) / number_viwe

    # Other initializations.
    Cluster_elem = {}
    for i in range(number_viwe): 
        Cluster_elem[i] = np.ones([k, row])/k
         
         
        
    dNK = np.zeros([row, k])
    dw = np.zeros([k])
    dv = np.zeros([number_viwe])
    # --------------------------------------------------------------------------
    
    print('Start of Fuzzy C-Means iterations')
    print('----------------------------------')

    # the algorithm iteration procedure
    while 1:
        
        landa =  Iter / row
        if number_viwe!=Iter:
            beta = Iter / number_viwe

        # Update the cluster assignments.
        for i in range(number_viwe):    
            col = data[i].shape[1]
            distance = np.zeros([k, row, col])
            
            pi = np.zeros([k, row])
            for ii in range(number_viwe):
                if ii==i:
                    continue
                pi = pi + Cluster_elem[ii]
                
            pi = pi * landa
            
            for j in range(k):
                distance = (data[i]-np.tile(center_points[i][j, :], (row, 1))) ** 2
                WBETA = z[i]**2
                WBETA[np.where(np.isinf(WBETA))] = 0
                dNK[:, j] = np.sum(w[i]**beta * distance * WBETA, 1)
    
            tmp1 = np.zeros([row, k])
            for j in range(k):
                tmp2 = (dNK / np.transpose(np.tile(dNK[:, j], (k, 1)))) ** (1 / (fuzzy_degree - 1))
                tmp2[np.where(np.isnan(tmp2))] = 0
                tmp2[np.where(np.isinf(tmp2))] = 0
                tmp1 = tmp1 + tmp2
    
            Cluster_elem[i] = (np.transpose(1 / tmp1)*(1 - np.sum(pi/(1+landa),0))) + (pi/(1+landa))
            Cluster_elem[i][np.where(np.isnan(Cluster_elem[i]))] = 1
            Cluster_elem[i][np.where(np.isinf(Cluster_elem[i]))] = 1
    
            for j in np.where(dNK == 0)[0]:
                Cluster_elem[i][np.where(dNK[j, :] == 0)[0], j] = 1 / len(np.where(dNK[j, :] == 0)[0])
                Cluster_elem[i][np.where(dNK[j, :] != 0)[0], j] = 0

        # Calculate the MinMax k-means objective.
        E_w = object_fun(row, col, k, Cluster_elem, center_points, fuzzy_degree, data, z, number_viwe, w, beta, landa)

        if math.isnan(E_w) == False:
            print(f'The algorithm objective is E_w={E_w}')

        # Check for convergence. Never converge if in the current (or previous)
        # iteration empty or singleton clusters were detected.
        if (math.isnan(E_w) == False) and (math.isnan(E_w_old) == False) and (abs(1 - E_w / E_w_old) < 10**-6 or Iter >= t_max):

            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(f'Converging for after {Iter} iterations.')
            print(f'The proposed algorithm objective is E_w={E_w}.')
            final = np.zeros([k, row])
            
            for i in range(number_viwe):
                Final = final + (w[i] * Cluster_elem[i])
                           
            return Final

        E_w_old = E_w

        # Update the cluster centers.
        for i in range(number_viwe): 
            
            col = data[i].shape[1]
            mf_prim =np.zeros([k, row])
            tmp5 =np.zeros([1, k, col])
            for ii in range(number_viwe):
                if ii==i:
                    continue
                mf_prim = mf_prim + ((Cluster_elem[i]-Cluster_elem[ii]) ** fuzzy_degree)
                tmp5 = tmp5 + np.matmul(np.expand_dims(((Cluster_elem[i]-Cluster_elem[ii]) ** fuzzy_degree), 0), data[i])               
            
            mf = Cluster_elem[i] ** fuzzy_degree  
            for j in range(k):
                tmp10 = ((np.matmul(np.expand_dims(mf[j, :], 0), data[i])) + (landa * (tmp5[:,j,:])))
                tmp11 = ((np.matmul(np.expand_dims(mf[j, :], 0), np.ones_like(data[i]))) + (landa * ((np.matmul(np.expand_dims(mf_prim[j, :], 0), np.ones_like(data[i]))))))         
                center_points[i][j, :] = tmp10 / tmp11

        
        # Update the feature weights.
        for i in range(number_viwe):
            col = data[i].shape[1]
            distance = np.zeros([k, row, col])
            dwkm= np.zeros([k, col])
            dwm= np.zeros([col])
            
            
            mf_prim =np.zeros([k, row])
            for ii in range(number_viwe):
                if ii==i:
                    continue
                mf_prim = mf_prim + ((Cluster_elem[i]-Cluster_elem[ii]) ** fuzzy_degree)
                
                
            for j in range(k):
                distance = (data[i]-np.tile(center_points[i][j, :], (row, 1))) ** 2
                dwkm[j, :] = np.matmul(( w[i]**beta * Cluster_elem[i][j, :] ** fuzzy_degree), distance)  + (landa * np.matmul(( w[i]**beta * mf_prim[j, :]), distance))
                
            dwm = np.sum(dwkm, 0)
    
            tmp1 = np.zeros([col])
            for j in range(col):
                tmp2 = (dwm / (np.tile(dwm[j], (1, col))))
                tmp2[np.where(np.isnan(tmp2))] = 0
                tmp2[np.where(np.isinf(tmp2))] = 0
                tmp1 = tmp1 + tmp2
    
            z[i] = (1 / tmp1)
            z[i][np.where(np.isnan(z[i]))] = 1
            z[i][np.where(np.isinf(z[i]))] = 1
    
            for j in np.where(dwm == 0)[0]:
                z[i][j, np.where(dwm[j, :] == 0)[0]] = 1 / len(np.where(dwm[j, :] == 0)[0])
                z[i][j, np.where(dwm[j, :] != 0)[0]] = 0
                
               
            # # Update the cluster weights.
        for i in range(number_viwe):
            col = data[i].shape[1]
            distance = np.zeros([k, row, col])
            dwkm= np.zeros([k, col])
            dwm= np.zeros([col])
            
            
            mf_prim =np.zeros([k, row])
            for ii in range(number_viwe):
                if ii==i:
                    continue
                mf_prim = mf_prim + ((Cluster_elem[i]-Cluster_elem[ii]) ** fuzzy_degree)
            
            
            for j in range(k):
                distance = (data[i]-np.tile(center_points[i][j, :], (row, 1))) ** 2
                WBETA = z[i]**2
                WBETA[np.where(np.isinf(WBETA))] = 0
                dw[j] = np.sum(WBETA * np.matmul((Cluster_elem[i][j, :] ** fuzzy_degree), distance))  + (landa * (np.sum(WBETA * np.matmul((mf_prim[j, :]), distance))))
            
            dv[i] = np.sum(dw)
                
                
        tmp = np.sum((np.tile(dv, (number_viwe, 1)) / np.transpose(np.tile(dv, (number_viwe, 1)))) ** (1/(beta-1)), axis=0)
        tmp[np.where(np.isnan(tmp))] = 0
        tmp[np.where(np.isinf(tmp))] = 0
        w = 1/tmp
        w[np.where(np.isnan(w))] = 1
        w[np.where(np.isinf(w))] = 1

        if len(np.where(dw == 0)[0]) > 0:
            w[np.where(dw == 0)[0]] = 1 / len(np.where(dw == 0)[0])
            w[np.where(dw != 0)[0]] = 0


        # check threshold
        for i in range(number_viwe):
            col = data[i].shape[1]
            threshold = 1 / (np.sqrt(row * col))     
            z[i][z[i] < threshold] = 0
            # normalize 
            z[i] = z[i] / np.sum(z[i])          

        Iter = Iter + 1
