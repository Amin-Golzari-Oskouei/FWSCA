def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))  # number of clusters.
    t_max = 100  # maximum number of iterations.
    Restarts = 10  # number of FCM restarts.
    fuzzy_degree = 2  # fuzzy membership degree

    # specific parameters
    if dataset == "balance":
        q = 3.8  # the exponent value for the feature weight updates (β parameter in the original Paper).
        sigma = 1000000
    elif dataset == "breast":
        q = 9.3
        sigma = 1
    elif dataset == "bupa":
        q = 1.2
        sigma = 100000
    elif dataset == "cancer":
        q = 7.6
        sigma = 10
    elif dataset == "Car_evaluation":
        q = 1
        sigma = 0.0000001
    elif dataset == "dermatology":
        q = 1
        sigma = 10
    elif dataset == "diabet":
        q = 10
        sigma = 10
    elif dataset == "ecoli":
        q = 1
        sigma = 10
    elif dataset == "glass":
        q = 1.1
        sigma = 10
    elif dataset == "heart":
        q = 1.1
        sigma = 1
    elif dataset == "heberman":
        q = 8
        sigma = 1
    elif dataset == "ionosphere":
        q = 1
        sigma = 10
    elif dataset == "iris":
        q = 2
        sigma = 1
    elif dataset == "letters":
        q = 9.7
        sigma = 100000
    elif dataset == "seed":
        q = 9.9
        sigma = 1
    elif dataset == "soybean":
        q = 1
        sigma = 10
    elif dataset == "spectfheart":
        q = 1.3
        sigma = 1
    elif dataset == "synthetic":
        q = 8.3
        sigma = 1000000
    elif dataset == "thyroid":
        q = 1.1
        sigma = 1
    elif dataset == "wine":
        q = 1.1
        sigma = 1
    elif dataset == "zoo":
        q = 1
        sigma = 10
    elif dataset == "cmc":
        q = 1
        sigma = 10
    elif dataset == "waveform":
        q = 1.8
        sigma = 1
    elif dataset == "vowel":
        q = 9.0
        sigma = 10000
    elif dataset == "breast_tissue":
        q = 1.1
        sigma = 100
    elif dataset == "synthetic_global":
        q = 10.0
        sigma = 100
        
        
    return k, t_max, Restarts, fuzzy_degree, q, sigma
