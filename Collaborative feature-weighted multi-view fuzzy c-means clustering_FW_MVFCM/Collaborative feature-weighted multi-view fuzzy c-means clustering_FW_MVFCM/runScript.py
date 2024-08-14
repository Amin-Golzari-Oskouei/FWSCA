from main import main
import numpy as np
import time
from calculateMetrics import calculateMetrics
# q, sigma, beta
def runScript(data, k, t_max, row, fuzzy_degree, number_viwe, Restarts, lable_true, dataSetName):
    with open(f'{dataSetName}.txt', 'w') as file:
        file.write('Collaborative feature-weighted multi-view fuzzy c-means clustering_FW_MVFCM\n\n')
        
        for t in np.arange(0.1, 5.2, 0.5):
                beta = round(t, 1)

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

                # Clustering the samples using the proposed procedure.
                for repeat in range(Restarts):

                    print(f'========================================================')
                    print(f'Proposed Algorithm: Restart {repeat+1}.')

                    # Randomly initialize the cluster centers.
                    for i in range(number_viwe):
                        center_points[i] = data[i][np.random.choice(data[i].shape[0], k, replace=False), :]

                    # Execute proposed algorithm.
                    # Get the cluster assignments and other parameters.
                    start_time = time.time()
                    Cluster_elem = main(data, center_points, k, t_max, row, fuzzy_degree, number_viwe, beta)
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

                    else:
                        ACC_repeat[repeat] = np.nan
                        NMI_repeat[repeat] = np.nan
                        PRE_repeat[repeat] = np.nan
                        REC_repeat[repeat] = np.nan
                        F_repeat[repeat] = np.nan
                        R_index_repeat[repeat] = np.nan

   

                str_Accurcy = f'Average accurcy score over {Restarts} restarts: {np.nanmean(ACC_repeat)}'
                str_NMI = f'Average NMI score over {Restarts} restarts: {np.nanmean(NMI_repeat)}'
                str_Precision = f'Average precision score  over {Restarts} restarts: {np.nanmean(PRE_repeat)}'
                str_Recall = f'Average recall score over {Restarts} restarts: {np.nanmean(REC_repeat)}'
                str_F1 = f'Average F1 score over {Restarts} restarts: {np.nanmean(F_repeat)}'
                str_DB = f'Average davies bouldin score over {Restarts} restarts: {np.nanmean(DBS_repeat)}'
                str_Silhouette = f'Average silhouette score over {Restarts} restarts: {np.nanmean(SI_repeat)}'
                str_Runtime = f'Average runtime over {Restarts} restarts: {np.nanmean(RunTime_repeat)}'
              
                result = f'\n\t\t===========beta={beta}============\n' + str_Accurcy + '\n' + str_NMI + '\n' + str_Precision + '\n' + str_Recall + '\n' + str_F1 + '\n' + str_DB + '\n' + str_Silhouette + '\n' + str_Runtime + '\n'

                with open(f'{dataSetName}.txt', 'a') as file:
                    file.write(result)

