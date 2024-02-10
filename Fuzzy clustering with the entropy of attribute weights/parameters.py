def parameters(dataset, lable_true, col, data):

    import numpy as np

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='iris':
        landa = 0.76
    elif dataset=='balance':
        landa = 0.01
    elif dataset=='breast':
        landa = 0.04
    elif dataset=='bupa':
        landa = 3.91
    elif dataset=='cancer':
        landa = 0.2
    elif dataset=='Car_evaluation':
        landa = 0.4
    elif dataset=='dermatology':
        landa = 0.8
    elif dataset=='diabet':
        landa = 1.7
    elif dataset=='ecoli':
        landa = 1.0
    elif dataset=='glass':
        landa = 5.0
    elif dataset=='heberman':
        landa = 3.0
    elif dataset=='ionosphere':
        landa = 0.1
    elif dataset=='heart':
        landa = 0.1
    elif dataset=='letters':
        landa = 0.1
    elif dataset=='seed':
        landa = 0.12
    elif dataset=='synthetic':
        landa = 0.07
    elif dataset=='spectfheart':
        landa = 3.86
    elif dataset=='zoo':
        landa = 0.2
    elif dataset=='wine':
        landa = 0.12
    elif dataset=='thyroid':
        landa = 0.55
    elif dataset=='soybean':
        landa = 1.34
        
    return k, t_max, Restarts, fuzzy_degree, landa

