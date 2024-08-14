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
        pa = 1
        pk = 1
        pm = 1
        alpha_type = 'PLOWA'               # 'PLOWA' , 'SOWA'
        loss_type = 'LOG-Linear'           # 'LOG-Linear', 'LOGarithmic', 'LINear', 'HUBer'
    elif dataset=='letters':
        q = 10 
    elif dataset=='seed':
        q = 6.6 
    elif dataset=='soybean':
        q = 1 
    elif dataset=='breast_tissue':
        pa = 0.9
        pk = 0.5  # 0.4 0.5 0.9
        pm = 0.9
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'Essential'  # 'LOG-Linear', 'LOGarithmic', 'SIGmoidal', 'Essential'
    elif dataset=='cmc':
        pa = 0.9
        pk = 0.9  # 0.4 0.5 0.9
        pm = 0.9  # 0.5 0.6 0.7 0.9
        alpha_type = 'PLOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'Essential'   # 'LOG-Linear', 'LOGarithmic', 'SIGmoidal', 'Essential'
    elif dataset=='synthetic_global':
        pa = 0.9
        pk = 0.3  # 0.4 0.5 0.9
        pm = 0.7  # 0.5 0.6 0.7 0.9
        alpha_type = 'PLOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'LOG-Linear'   # 'LOG-Linear', 'LOGarithmic', 'SIGmoidal', 'Essential'
    elif dataset=='vowel':
        pa = 0.9
        pk = 0.3  # 0.4 0.5 0.9
        pm = 0.3  # 0.5 0.6 0.7 0.9
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'SIGmoidal'   # 'LOG-Linear', 'LOGarithmic', 'SIGmoidal', 'Essential'
    elif dataset=='waveform':
        pa = 0.9
        pk = 0.3  # 0.4 0.5 0.9
        pm = 0.3  # 0.5 0.6 0.7 0.9
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'LOG-Linear'   # 'LOG-Linear', 'LOGarithmic', 'SIGmoidal', 'Essential'



    return k, t_max, Restarts, fuzzy_degree, pa, pk , pm, alpha_type, loss_type