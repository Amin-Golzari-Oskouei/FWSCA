def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='balance':
        q = 3.9                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='breast':
        q = 9.5 
    elif dataset=='bupa':
        q = 1.3 
    elif dataset=='cancer':
        q = 10
    elif dataset=='Car_evaluation':
        q = 1 
    elif dataset=='dermatology':
        q = 1 
    elif dataset=='diabet':
        q = 10 
    elif dataset=='ecoli':
        q = 1 
    elif dataset=='glass':
        q = 5.4 
    elif dataset=='heart':
        q = 9.7 
    elif dataset=='heberman':
        q = 9.6 
    elif dataset=='ionosphere':
        q = 1 
    elif dataset=='iris':
        q = 2
        pa = 1
        pk = 1
        pm = 1
        alpha_type = 'SOWA'               # 'PLOWA' , 'SOWA'
        loss_type = 'Essential'              #'Essential' , 'LOG-Linear', 'LOGarithmic', 'LINear', 'HUBer'
    elif dataset=='letters':
        q = 10 
    elif dataset=='seed':
        q = 6.6 
    elif dataset=='soybean':
        q = 1 
    elif dataset=='spectfheart':
        q = 1.3 
    elif dataset=='synthetic':
        q = 8.7 
    elif dataset=='thyroid':
        q = 8.6 
    elif dataset=='wine':
        q = 9.7 
    elif dataset=='zoo':
        q = 1 
    return k, t_max, Restarts, fuzzy_degree, q, pa, pk , pm, alpha_type, loss_type