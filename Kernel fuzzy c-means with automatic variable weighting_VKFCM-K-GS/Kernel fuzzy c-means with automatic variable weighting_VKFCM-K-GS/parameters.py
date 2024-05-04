def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='balance':
        q = 5.4                     # the exponent value for the feature weight updates (β parameter in the original Paper).
        sigma = 10000
    elif dataset=='breast':
        q = 2.6 
        sigma = 10
    elif dataset=='bupa':
        q = 2.5 
        sigma = 0.01
    elif dataset=='cancer':
        q = 1
        sigma = 1
    elif dataset=='Car_evaluation':
        q = 1 
        sigma = 1
    elif dataset=='dermatology':
        q = 1 
        sigma = 1
    elif dataset=='diabet':
        q = 1 
        sigma = 1
    elif dataset=='ecoli':
        q = 1 
        sigma = 1
    elif dataset=='glass':
        q = 1 
        sigma = 1
    elif dataset=='heart':
        q = 1 
        sigma = 1
    elif dataset=='heberman':
        q = 1.3
        sigma = 0.01 
    elif dataset=='ionosphere':
        q=1
        sigma = 1 
    elif dataset=='iris':
        q = 2.5 
        sigma = 1000000
    elif dataset=='letters':
        sigma = 1.6
        q = 100
    elif dataset=='seed':
        q = 8.5 
        sigma = 1
    elif dataset=='soybean':
        q = 1.1 
        sigma = 0.001
    elif dataset=='spectfheart':
        q = 5.5
        sigma = 0.1
    elif dataset=='synthetic':
        q = 9.7
        sigma = 1
    elif dataset=='thyroid':
        q = 6.7 
        sigma = 100
    elif dataset=='wine':
        q = 10.0 
        sigma = 1

    return k, t_max, Restarts, fuzzy_degree, q, sigma
