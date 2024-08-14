def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='iris':
        sigma = 1
    elif dataset=='balance':
        sigma = 1000000
    elif dataset=='breast':
        sigma = 10
    elif dataset=='bupa':
        sigma = 0.01
    elif dataset=='cancer':
        sigma = 100
    elif dataset=='Car_evaluation':
        sigma = 0.0000001
    elif dataset=='dermatology':
        sigma = 10
    elif dataset=='diabet':
        sigma = 100000
    elif dataset=='ecoli':
        sigma = 10
    elif dataset=='glass':
        sigma = 0.0001
    elif dataset=='heberman':
        sigma = 0.01
    elif dataset=='ionosphere':
        sigma = 10
    elif dataset=='heart':
        sigma = 10
    elif dataset=='letters':
        sigma = 1
    elif dataset=='seed':
        sigma = 100000
    elif dataset=='synthetic':
        sigma = 0.1
    elif dataset=='spectfheart':
        sigma = 0.1
    elif dataset=='zoo':
        sigma = 10
    elif dataset=='wine':
        sigma = 0.0001
    elif dataset=='thyroid':
        sigma = 1000000
    elif dataset=='soybean':
        sigma = 10
    elif dataset=='cmc':
        sigma = 10
    elif dataset=='synthetic_global':
        sigma = 100
    elif dataset=='vowel':
        sigma = 1
    elif dataset=='waveform':
        sigma = 0.1
    elif dataset=='breast_tissue':
        sigma = 10
        
    return k, t_max, Restarts, fuzzy_degree, sigma