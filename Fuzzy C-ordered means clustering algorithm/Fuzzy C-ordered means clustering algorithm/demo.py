# This demo shows how to call the extention of fuzzy C-means algorithm 
# For the demonstration, the Iris dataset of the above paper is used.
# Courtesy of A.Golzari Oskouei
# Contributors: A.Golzari Oskouei & Hamidreza Babaei
import numpy as np
from main import main
from calculateMetrics import calculateMetrics
import scipy.io
from parameters import parameters
import time
import os

# Load the dataset.
datasets=['iris']
for dataset in datasets:
    
    mat = scipy.io.loadmat(f'{dataset}'+'.mat')
    data = mat[f'{dataset}']

    lable_true = data[:, -1]
    data = data[:, 0:-1]
    [row, col] = data.shape

    data = (data-data.min())/(data.max()-data.min())  # normalized data

    # Algorithm parameters.
    k, t_max, Restarts, fuzzy_degree, pa, pk , pm, alpha_type, loss_type = parameters(dataset, lable_true)

    # initializations.
    np.random.seed(1373)
    ACC_repeat = np.empty([Restarts])
    NMI_repeat = np.empty([Restarts])
    PRE_repeat = np.empty([Restarts])
    REC_repeat = np.empty([Restarts])
    F_repeat = np.empty([Restarts])
    DBS_repeat = np.empty([Restarts])
    SI_repeat = np.empty([Restarts])
    RunTime_repeat = np.empty([Restarts])

    # --------------------------------------------------------
    # Clustering the samples using the proposed procedure.
    # --------------------------------------------------------
    
    for repeat in range(Restarts):
        print(f'========================================================')
        print(f'Proposed Algorithm: Restart {repeat+1}.')

        # Randomly initialize the cluster centers.
        center_points = data[np.random.choice(data.shape[0], k, replace=False), :]

        # Execute proposed algorithm.
        # Get the cluster assignments and other parameters.
        start_time = time.time()
        Cluster_elem = main(data, center_points, k, t_max, row, fuzzy_degree, col, pa, pk , pm, alpha_type, loss_type)
        end_time = time.time()

        RunTime_repeat[repeat] = end_time - start_time

        lable_pre = Cluster_elem.argmax(axis=0)

        if Cluster_elem is not None and len(np.unique(lable_pre))==k:
            ans = calculateMetrics(lable_pre, lable_true, row, data)
            ACC_repeat[repeat] = ans[0]
            NMI_repeat[repeat] = ans[1]
            PRE_repeat[repeat] = ans[2]
            REC_repeat[repeat] = ans[3]
            F_repeat[repeat] = ans[4]
            DBS_repeat[repeat] = ans[5]
            SI_repeat[repeat] = ans[6]

            print(f'The accurcy score in {repeat+1}th  Restart is {ans[0]}.')
            print(f'The NMI score in {repeat+1}th  Restart is {ans[1]}.')
            print(f'The precision score in {repeat+1}th  Restart is {ans[2]}.')
            print(f'The recall score in {repeat+1}th  Restart is {ans[3]}.')
            print(f'The F1 score in {repeat+1}th  Restart is {ans[4]}.')
            print(f'The davies bouldin score in {repeat+1}th  Restart is {ans[5]}.')
            print(f'The silhouette score in {repeat+1}th  Restart is {ans[6]}.')
            print(f'The runtime in {repeat+1}th  Restart is {RunTime_repeat[repeat]}.')
            print(f'End of Restart {repeat + 1}')

            print('========================================================')
        else:
            ACC_repeat[repeat] = np.nan
            NMI_repeat[repeat] = np.nan
            PRE_repeat[repeat] = np.nan
            REC_repeat[repeat] = np.nan
            F_repeat[repeat] = np.nan
            DBS_repeat[repeat] = np.nan
            SI_repeat[repeat] = np.nan

            print(f'The accurcy score in {repeat+1}th  Restart is NaN.')
            print(f'The NMI score in {repeat+1}th  Restart is NaN.')
            print(f'The precision score in {repeat+1}th  Restart is NaN.')
            print(f'The recall score in {repeat+1}th  Restart is NaN.')
            print(f'The F1 score in {repeat+1}th  Restart is NaN.')
            print(f'The davies bouldin score in {repeat+1}th  Restart is NaN.')
            print(f'The silhouette score in {repeat+1}th  Restart is NaN.')
            print(f'The runtime in {repeat+1}th  Restart is {RunTime_repeat[repeat]}.')

            print(f'End of Restart {repeat + 1}')
            print('========================================================')

    print(f'Average accurcy score over {Restarts} restarts: {np.nanmean(ACC_repeat)}')
    print(f'Average NMI score over {Restarts} restarts: {np.nanmean(NMI_repeat)}')
    print(f'Average precision score  over {Restarts} restarts: {np.nanmean(PRE_repeat)}')
    print(f'Average recall score over {Restarts} restarts: {np.nanmean(REC_repeat)}')
    print(f'Average F1 score over {Restarts} restarts: {np.nanmean(F_repeat)}')
    print(f'Average davies bouldin score over {Restarts} restarts: {np.nanmean(DBS_repeat)}')
    print(f'Average silhouette score over {Restarts} restarts: {np.nanmean(SI_repeat)}')
    print(f'Average runtime over {Restarts} restarts: {np.nanmean(RunTime_repeat)}')
