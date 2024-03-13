def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='iris':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='balance':
        pass
    elif dataset=='breast':
        pass
    elif dataset=='bupa':
        pass
    elif dataset=='cmc':
        pass
    elif dataset=='coil2':
        pass
    elif dataset=='dermatology':
        pass
    elif dataset=='ecoli':
        pass
    elif dataset=='fertility':
        pass
    elif dataset=='glass':
        pass
    elif dataset=='seed':
        pass
    elif dataset=='seismic':
        pass
    elif dataset=='zoo':
        pass
    elif dataset=='wine':
        pass
    elif dataset=='vowel':
        pass
    elif dataset=='thyroid':
        pass
    elif dataset=='soybean':
        pass
    return k, t_max, Restarts, fuzzy_degree, A