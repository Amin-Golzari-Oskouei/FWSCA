def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree
    T_pow = 2;                   # power of T


    # specific parameters
    if dataset=='iris':
            a_coefficient = 1;           # coefficient of u
            b_coefficient = 1;           # coefficient of t
            balance_tarm = 1;            # balance parameter among to terms of loss function
    elif dataset=='balance':
        pass
    elif dataset=='breast':
        pass
    elif dataset=='bupa':
        pass
    elif dataset=='cancer':
        pass
    elif dataset=='Car_evaluation':
        pass
    elif dataset=='dermatology':
        pass
    elif dataset=='diabet':
        pass
    elif dataset=='ecoli':
        pass
    elif dataset=='glass':
        pass
    elif dataset=='heberman':
        pass
    elif dataset=='ionosphere':
        pass
    elif dataset=='heart':
        pass
    elif dataset=='letters':
        pass
    elif dataset=='seed':
        pass
    elif dataset=='seismic':
        pass
    elif dataset=='synthetic':
        pass
    elif dataset=='spectfheart':
        pass
    elif dataset=='zoo':
        pass
    elif dataset=='wine':
        pass
    elif dataset=='thyroid':
        pass
    elif dataset=='soybean':
        pass
        
    return k, t_max, Restarts, fuzzy_degree, T_pow, a_coefficient, b_coefficient, balance_tarm