def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='balance':
        q = 1.2                     # the exponent value for the feature weight updates (β parameter in the original Paper).
        sigma = 10
    elif dataset=='breast':
        q = 2.1 
        sigma = 0.000001
    elif dataset=='bupa':
        q = 1.1 
        sigma = 100
    elif dataset=='cancer':
        q = 1.1
        sigma = 100
    elif dataset=='Car_evaluation':
        q = 1 
        sigma = 0.000001
    elif dataset=='dermatology':
        q = 1 
        sigma = 10
    elif dataset=='diabet':
        q = 6.7 
        sigma = 100
    elif dataset=='ecoli':
        q = 1 
        sigma = 10
    elif dataset=='glass':
        q = 5.4 
        sigma = 0.0001
    elif dataset=='heart':
        q = 1.1 
        sigma = 10
    elif dataset=='heberman':
        q = 1.1
        sigma = 100 
    elif dataset=='ionosphere':
        sigma = 10 
    elif dataset=='iris':
        q = 1.1 
        sigma = 10
    elif dataset=='letters':
	q = 7.5 
        sigma = 10
    elif dataset=='seed':
        q = 1.1 
        sigma = 0.000001
    elif dataset=='soybean':
        q = 1 
        sigma = 10
    elif dataset=='spectfheart':
        q = 1.1
        sigma = 10
    elif dataset=='synthetic':
        q = 1.1 
        sigma = 100
    elif dataset=='thyroid':
        q = 6.7 
        sigma = 100
    elif dataset=='wine':
        q = 1.6 
        sigma = 100
    elif dataset=='zoo':
        q = 1 
        sigma = 10
    return k, t_max, Restarts, fuzzy_degree, q, sigma
