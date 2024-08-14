# This demo shows how to call the extention of fuzzy C-means algorithm 
# For the demonstration, the Iris dataset of the above paper is used.
# Courtesy of A.Golzari Oskouei

import numpy as np
from main import main
from calculateMetrics import calculateMetrics
import scipy.io
from parameters import parameters
import time
from runScript import runScript
import os
# Load the dataset.
datasets=['prokaryotic']
for dataset in datasets:
    
    mat = scipy.io.loadmat(f'{dataset}'+'.mat')
    data = {}
    data[0] = np.array(mat['gene_repert'])
    data[1] = np.array(mat['text'])
    data[2] = np.array(mat['proteome_comp'])
    lable_true = np.squeeze(np.array(mat['truth']))

    row = len(lable_true)
    number_viwe = len(data)

    for i in range(number_viwe):
        data[i] = (data[i]-data[i].min())/(data[i].max()-data[i].min())  # normalized data

    # Algorithm parameters.
    k, t_max, Restarts, fuzzy_degree, beta, landa =parameters(dataset, lable_true)

    # initializations.
    np.random.seed(1373)
    ACC_repeat = np.empty([Restarts])
    NMI_repeat = np.empty([Restarts])
    PRE_repeat = np.empty([Restarts])
    REC_repeat = np.empty([Restarts])
    F_repeat = np.empty([Restarts])
    DBS_repeat = np.empty([Restarts])
    SI_repeat = np.empty([Restarts])
    R_index_repeat = np.empty([Restarts])
    RunTime_repeat = np.empty([Restarts])
    center_points = {}

    # --------------------------------------------------------
    # Clustering the samples using the proposed procedure.
    # --------------------------------------------------------

    runScript(data, k, t_max, row, fuzzy_degree, number_viwe, Restarts, lable_true, dataset)

    for repeat in range(Restarts):
        print(f'========================================================')
        print(f'Proposed Algorithm: Restart {repeat+1}.')


        # Randomly initialize the cluster centers.
        for i in range(number_viwe):
            center_points[i] = data[i][np.random.choice(data[i].shape[0], k, replace=False), :]

        # Execute proposed algorithm.
        # Get the cluster assignments and other parameters.
        start_time = time.time()
        Cluster_elem = main(data, center_points, k, t_max, row, fuzzy_degree, number_viwe, beta, landa)
        end_time = time.time()

        RunTime_repeat[repeat] = end_time - start_time

        lable_pre = Cluster_elem.argmax(axis=0)

        if Cluster_elem is not None and len(np.unique(lable_pre))==k:
            ans = calculateMetrics(lable_pre, lable_true, row)
            ACC_repeat[repeat] = ans[0]
            NMI_repeat[repeat] = ans[1]
            PRE_repeat[repeat] = ans[2]
            REC_repeat[repeat] = ans[3]
            F_repeat[repeat] = ans[4]
            R_index_repeat[repeat] = ans[5]


            # print(f'The accurcy score in {repeat+1}th  Restart is {ans[0]}.')
            # print(f'The NMI score in {repeat+1}th  Restart is {ans[1]}.')
            # print(f'The precision score in {repeat+1}th  Restart is {ans[2]}.')
            # print(f'The recall score in {repeat+1}th  Restart is {ans[3]}.')
            # print(f'The F1 score in {repeat+1}th  Restart is {ans[4]}.')
            # print(f'The R_index score in {repeat+1}th  Restart is {ans[5]}.')
            # print(f'The runtime in {repeat+1}th  Restart is {RunTime_repeat[repeat]}.')
            # print(f'End of Restart {repeat + 1}')

            # print('========================================================')
        else:
            ACC_repeat[repeat] = np.nan
            NMI_repeat[repeat] = np.nan
            PRE_repeat[repeat] = np.nan
            REC_repeat[repeat] = np.nan
            F_repeat[repeat] = np.nan
            R_index_repeat[repeat] = np.nan

    #         print(f'The accurcy score in {repeat+1}th  Restart is NaN.')
    #         print(f'The NMI score in {repeat+1}th  Restart is NaN.')
    #         print(f'The precision score in {repeat+1}th  Restart is NaN.')
    #         print(f'The recall score in {repeat+1}th  Restart is NaN.')
    #         print(f'The F1 score in {repeat+1}th  Restart is NaN.')
    #         print(f'The R_index score in {repeat+1}th  Restart is NaN.')

    #         print(f'The runtime in {repeat+1}th  Restart is {RunTime_repeat[repeat]}.')

    #         print(f'End of Restart {repeat + 1}')
    #         print('========================================================')

    # print(f'Average accurcy score over {Restarts} restarts: {np.nanmean(ACC_repeat)}')
    # print(f'Average NMI score over {Restarts} restarts: {np.nanmean(NMI_repeat)}')
    # print(f'Average precision score  over {Restarts} restarts: {np.nanmean(PRE_repeat)}')
    # print(f'Average recall score over {Restarts} restarts: {np.nanmean(REC_repeat)}')
    # print(f'Average F1 score over {Restarts} restarts: {np.nanmean(F_repeat)}')
    # print(f'Average R_index score over {Restarts} restarts: {np.nanmean(R_index_repeat)}')
    # print(f'Average runtime over {Restarts} restarts: {np.nanmean(RunTime_repeat)}')
