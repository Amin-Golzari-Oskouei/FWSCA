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
        sigma = 1000000
    elif dataset == "breast":
        sigma = 1
    elif dataset == "bupa":
        sigma = 1000000
    elif dataset == "cancer":
        sigma = 10
    elif dataset == "Car_evaluation":
        sigma = 1000
    elif dataset == "dermatology":
        sigma = 1
    elif dataset == "diabet":
        sigma = 1000
    elif dataset == "ecoli":
        sigma = 1
    elif dataset == "glass":
        sigma = 1
    elif dataset == "heberman":
        sigma = 1000000
    elif dataset == "ionosphere":
        sigma = 1
    elif dataset == "heart":
        sigma = 10
    elif dataset == "letters":
        sigma = 1000000
    elif dataset == "seed":
        sigma = 10
    elif dataset == "synthetic":
        sigma = 10
    elif dataset == "spectfheart":
        sigma = 10
    elif dataset == "zoo":
        sigma = 1
    elif dataset == "wine":
        sigma = 1
    elif dataset == "thyroid":
        sigma = 1
    elif dataset == "soybean":
        sigma = 1
    elif dataset == "cmc":
        sigma = 100000      
    elif dataset == "waveform":
        sigma = 0.1  
    elif dataset == "vowel":
        sigma = 1000000
    elif dataset == "breast_tissue":
        sigma = 0.1
    elif dataset == "synthetic_global":
        sigma = 100

    return k, t_max, Restarts, fuzzy_degree, sigma