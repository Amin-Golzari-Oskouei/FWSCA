def parameters(dataset, lable_true, col, data):

    import numpy as np

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset == 'iris':
        landa = 3.7
        sigma = 1
    elif dataset == 'balance':
        landa = 0.2
        sigma = 0.1
    elif dataset == 'breast':
        landa = 3.5
        sigma = 1000
    elif dataset == 'bupa':
        landa = 0.2
        sigma = 0.1
    elif dataset == 'cancer':
        landa = 0.7
        sigma = 10
    elif dataset == 'Car_evaluation':
        landa = 1.3
        sigma = 0.1
    elif dataset == 'dermatology':
        landa = 1.0
        sigma = 10
    elif dataset == 'diabet':
        landa = 5.0
        sigma = 10
    elif dataset == 'ecoli':
        landa = 1.0
        sigma = 10
    elif dataset == 'glass':
        landa = 5.0
        sigma = 1
    elif dataset == 'heberman':
        landa = 4.6
        sigma = 1
    elif dataset == 'ionosphere':
        landa = 0.8
        sigma = 10
    elif dataset == 'heart':
        landa = 0.9
        sigma = 1
    elif dataset == 'letters':
        landa = 0.6
        sigma = 10
    elif dataset == 'zoo':
        landa = 1.0
        sigma = 10
    elif dataset == 'wine':
        landa = 0.6
        sigma = 1
    elif dataset == 'seed':
        landa = 5.0
        sigma = 1
    elif dataset == 'thyroid':
        landa = 0.7
        sigma = 1
    elif dataset == 'soybean':
        landa = 1.4
        sigma = 1
    elif dataset == 'synthetic':
        landa = 0.2
        sigma = 1
    elif dataset == 'spectfheart':
        landa = 3.8
        sigma = 0.1
    elif dataset == 'cmc':
        landa = 3.1
        sigma = 0.1
    elif dataset == 'vowel':
        landa = 1.6
        sigma = 100000
    elif dataset == 'waveform':
        landa = 3.8
        sigma = 0.1
    elif dataset == 'synthetic_global':
        landa = 3.1
        sigma = 100000
    elif dataset == 'breast_tissue':
        landa = 1.1
        sigma = 0.1

    return k, t_max, Restarts, fuzzy_degree, landa, sigma
