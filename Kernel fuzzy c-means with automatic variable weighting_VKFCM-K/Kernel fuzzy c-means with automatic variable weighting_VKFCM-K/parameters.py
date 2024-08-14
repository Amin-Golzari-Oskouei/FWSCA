def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))  # number of clusters.
    t_max = 100  # maximum number of iterations.
    Restarts = 10  # number of FCM restarts.
    fuzzy_degree = 2  # fuzzy membership degree

    # specific parameters
    if dataset == "iris":
        sigma = 1
    elif dataset == "balance":
        sigma = 100000
    elif dataset == "breast":
        sigma = 10
    elif dataset == "bupa":
        sigma = 0.1
    elif dataset == "cancer":
        sigma = 0.1
    elif dataset == "Car_evaluation":
        sigma = 0.000001
    elif dataset == "dermatology":
        sigma = 1
    elif dataset == "diabet":
        sigma = 10
    elif dataset == "ecoli":
        sigma = 10
    elif dataset == "glass":
        sigma = 10
    elif dataset == "heberman":
        sigma = 0.01
    elif dataset == "ionosphere":
        sigma = 10
    elif dataset == "heart":
        sigma = 0.0001
    elif dataset == "letters":
        sigma = 1
    elif dataset == "seed":
        sigma = 1
    elif dataset == "synthetic":
        sigma = 1
    elif dataset == "spectfheart":
        sigma = 0.1
    elif dataset == "zoo":
        sigma = 10
    elif dataset == "wine":
        sigma = 0.1
    elif dataset == "thyroid":
        sigma = 1000000
    elif dataset == "soybean":
        sigma = 1
    elif dataset == "synthetic_global":
        sigma = 0.01
    elif dataset == "vowel":
        sigma = 0.1
    elif dataset == "waveform":
        sigma = 0.1
    elif dataset == "breast_tissue":
        sigma = 0.001
    elif dataset == "cmc":
        sigma = 0.01

    return k, t_max, Restarts, fuzzy_degree, sigma
