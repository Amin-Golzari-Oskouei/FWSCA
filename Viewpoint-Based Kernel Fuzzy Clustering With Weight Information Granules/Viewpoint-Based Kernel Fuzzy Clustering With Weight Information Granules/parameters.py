def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 1                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='iris':
        landa = 1.4               # the exponent α in orginal paper.
        sigma = 1                 # σ parameter of kenel.
    elif dataset == 'balance':
        landa = 0.8
        sigma = 0.1
    elif dataset == 'breast':
        landa = 0.1
        sigma = 10
    elif dataset == 'bupa':
        landa = 1.1
        sigma = 0.01
    elif dataset == 'cancer':
        landa = 0.5
        sigma = 100
    elif dataset == 'Car_evaluation':
        landa = 0.5
        sigma = 0.0000001
    elif dataset == 'dermatology':
        landa = 1
        sigma = 10
    elif dataset == 'diabet':
        landa = 1
        sigma = 0.000001
    elif dataset == 'ecoli':
        landa = 1
        sigma = 10
    elif dataset == 'glass':
        landa = 0.7
        sigma = 0.0001
    elif dataset == 'heberman':
        landa = 1.1
        sigma = 0.01
    elif dataset == 'ionosphere':
        landa = 1
        sigma = 10
    elif dataset == 'heart':
        landa = 1.3
        sigma = 10
    elif dataset == 'letters':
        landa = 1.7
        sigma = 1
    elif dataset == 'seed':
        landa = 0.7
        sigma = 100000
    elif dataset == 'synthetic':
        landa = 1.3
        sigma = 0.1
    elif dataset == 'spectfheart':
        landa = 8.3

        sigma = 0.1
    elif dataset == 'zoo':
        landa = 1
        sigma = 10
    elif dataset == 'wine':
        landa = 1.3
        sigma = 0.0001
    elif dataset == 'thyroid':
        landa = 1
        sigma = 1000000
    elif dataset == 'soybean':
        landa = 1
        sigma = 10
    return k, t_max, Restarts, fuzzy_degree, landa, sigma