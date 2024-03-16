def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='balance':
        q = 3.9                     # the exponent value for the feature weight updates (β parameter in the original Paper).
        sigma = 1000000
    elif dataset=='breast':
        q = 9.5 
        sigma = 10
    elif dataset=='bupa':
        q = 1.3 
        sigma = 0.01
    elif dataset=='cancer':
        q = 10
        sigma = 100
    elif dataset=='Car_evaluation':
        q = 1 
        sigma = 0.0000001
    elif dataset=='dermatology':
        q = 1 
        sigma = 10
    elif dataset=='diabet':
        q = 10 
        sigma = 100000
    elif dataset=='ecoli':
        q = 1 
        sigma = 10
    elif dataset=='glass':
        q = 5.4 
        sigma = 0.0001
    elif dataset=='heart':
        q = 9.7 
        sigma = 10
    elif dataset=='heberman':
        q = 9.6 
        sigma = 0.01 
    elif dataset=='ionosphere':
        sigma = 10 
    elif dataset=='iris':
        q = 2 
        sigma = 1
    elif dataset=='letters':
        sigma = 1 
    elif dataset=='seed':
        q = 6.6 
        sigma = 100000
    elif dataset=='soybean':
        q = 1 
        sigma = 10
    elif dataset=='spectfheart':
        q = 1.3 
        sigma = 0.1
    elif dataset=='synthetic':
        q = 8.7 
        sigma = 0.1
    elif dataset=='thyroid':
        q = 8.6 
        sigma = 1000000
    elif dataset=='wine':
        q = 9.7 
        sigma = 0.0001
    elif dataset=='zoo':
        q = 1 
        sigma = 10
    return k, t_max, Restarts, fuzzy_degree, q, sigma