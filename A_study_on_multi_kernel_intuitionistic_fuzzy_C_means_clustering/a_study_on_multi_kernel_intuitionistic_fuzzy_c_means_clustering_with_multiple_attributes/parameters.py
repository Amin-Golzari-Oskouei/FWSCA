def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='iris':
        beta = 0.9                # the exponent α in orginal paper.
        q = 3                     # the exponent value for the feature weight updates (β parameter in the original Paper).
        sigma = 1                 # σ parameter of kenel.
    elif dataset == 'balance':
        beta = 1.1
        q = 5
        sigma = 1
    elif dataset == 'breast':
        beta = 0.1
        q = 9
        sigma = 10
    elif dataset == 'bupa':
        beta = 1.1
        q = 3
        sigma = 0.01
    elif dataset == 'cancer':
        beta = 0.5
        q = 10
        sigma = 100
    elif dataset == 'Car_evaluation':
        beta = 0.5
        q = 10
        sigma = 0.0000001
    elif dataset == 'dermatology':
        beta = 1
        q = 2
        sigma = 10
    elif dataset == 'diabet':
        beta = 1.5
        q = 5
        sigma = 100000
    elif dataset == 'ecoli':
        beta = 1
        q = 2
        sigma = 10
    elif dataset == 'glass':
        beta = 0.7
        q = 7
        sigma = 0.0001
    elif dataset == 'heberman':
        beta = 1.1
        q = 5
        sigma = 0.0000001
    elif dataset == 'ionosphere':
        beta = 1
        q = 2
        sigma = 10
    elif dataset == 'heart':
        beta = 1.3
        q = 9
        sigma = 10
    elif dataset == 'letters':
        beta = 1.7
        q = 10
        sigma = 1
    elif dataset == 'seed':
        beta = 0.7
        q = 10
        sigma = 100000
    elif dataset == 'synthetic':
        beta = 1.3
        q = 3
        sigma = 0.1
    elif dataset == 'spectfheart':
        beta = 8.3
        q = 10
        sigma = 0.1
    elif dataset == 'zoo':
        beta = 1
        q = 2
        sigma = 10
    elif dataset == 'wine':
        beta = 1.3
        q = 4
        sigma = 0.0001
    elif dataset == 'thyroid':
        beta = 1
        q = 2
        sigma = 1000000
    elif dataset == 'soybean':
        beta = 1
        q = 2
        sigma = 10
    return k, t_max, Restarts, fuzzy_degree, beta, q, sigma
