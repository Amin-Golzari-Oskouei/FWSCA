def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 1                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='iris':
        landa = 1.3               # the exponent α in orginal paper.
        sigma = 1                 # σ parameter of kenel.
    elif dataset == 'balance':
        landa = 0.1
        sigma = 100000
    elif dataset == 'breast':
        landa = 1
        sigma = 1.6
    elif dataset == 'bupa':
        landa = 0.4
        sigma = 0.01
    elif dataset == 'cancer':
        landa = 0.4
        sigma = 0.1
    elif dataset == 'Car_evaluation':
        landa = 0.1
        sigma = 0.1
    elif dataset == 'dermatology':
        landa = 1.6
        sigma = 100
    elif dataset == 'diabet':
        landa = 0.3
        sigma = 0.001
    elif dataset == 'ecoli':
        landa = 1
        sigma = 10
    elif dataset == 'glass':
        landa = 7.2
        sigma = 1
    elif dataset == 'heberman':
        landa = 3.5
        sigma = 0.1
    elif dataset == 'ionosphere':
        landa = 0.2
        sigma = 10
    elif dataset == 'heart':
        landa = 0.7
        sigma = 0.001
    elif dataset == 'letters':
        landa = 1.8
        sigma = 1
    elif dataset == 'seed':
        landa = 3.5
        sigma = 0.1
    elif dataset == 'synthetic':
        landa = 4.5
        sigma = 100
    elif dataset == 'spectfheart':
        landa = 0.1
        sigma = 0.1
    elif dataset == 'zoo':
        landa = 6.4
        sigma = 0.1
    elif dataset == 'wine':
        landa = 9.9
        sigma = 0.0001
    elif dataset == 'thyroid':
        landa = 2.6
        sigma = 10
    elif dataset == 'soybean':
        landa = 2.2
        sigma = 10
    elif dataset == 'cmc':
        landa = 1.8
        sigma = 0.1
    elif dataset == 'synthetic_global':
        landa = 9.5
        sigma = 0.1
    elif dataset == 'waveform':
        landa = 0.1
        sigma = 1000
        
    elif dataset == 'breast_tissue':
        landa = 5.1
        sigma = 0.01
    elif dataset == 'vowel':
        landa = 0.1
        sigma = 1
    return k, t_max, Restarts, fuzzy_degree, landa, sigma