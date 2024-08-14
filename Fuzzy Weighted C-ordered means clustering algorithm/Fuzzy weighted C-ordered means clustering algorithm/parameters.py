def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree


    # ====alpha=PLOWA====//loss=Essential====//pa=0.9====//pk=0.5====//pm=0.9==== breast_tissue
    # ====alpha=PLOWA====//loss=Essential====//pa=0.9====//pk=0.5====//pm=0.9==== cmc
    # ====alpha=PLOWA====//loss=SIGmoidal====//pa=0.9====//pk=0.9====//pm=0.9==== synthetic_global
    # ====alpha=SOWA====//loss=SIGmoidal====//pa=0.9====//pk=0.3====//pm=0.9==== vowel
    # ====alpha=SOWA====//loss=LOG-Linear====//pa=0.9====//pk=0.3====//pm=0.3==== waveform
    # specific parameters
    if dataset=='breast_tissue':
        q = 6
        pa = 0.9
        pk = 0.5
        pm = 0.9
        alpha_type = 'PLOWA'
        loss_type = 'Essential'
    elif dataset=='cmc':
        q = 6
        pa = 0.4
        pk = 0.5
        pm = 0.7
        alpha_type = 'PLOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'Essential'
    elif dataset=='synthetic_global':
        q = 6
        pa = 0.9
        pk = 0.9
        pm = 0.9
        alpha_type = 'PLOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'SIGmoidal'
    elif dataset=='vowel':
        q = 6
        pa = 0.9
        pk = 0.9
        pm = 0.6
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'SIGmoidal' 
    elif dataset=='waveform':
        q = 6
        pa = 0.9
        pk = 0.3
        pm = 0.3
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'LOG-Linear' 
    elif dataset=='glass':
        q = 6
        pa = 0.9
        pk = 0.9
        pm = 0.9
        alpha_type = 'PLOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'Essential' 
    elif dataset=='heberman':
        q = 10
        pa = 0.9
        pk = 0.3
        pm = 0.3
        alpha_type = 'PLOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'LOG-Linear' 
    elif dataset=='ionosphere':
        q = 1
        pa = 0.9
        pk = 0.9
        pm = 0.6
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'SIGmoidal'  
    elif dataset=='iris':
        q = 8
        pa = 0.9
        pk = 0.9
        pm = 0.9
        alpha_type = 'PLOWA'# 'PLOWA' , 'SOWA'
        loss_type = 'LOGarithmic' #'Essential' , 'LOG-Linear', 'LOGarithmic', 'LINear', 'HUBer'
    elif dataset=='letters':
        q = 10
        pa = 0.9
        pk = 0.9
        pm = 0.6
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'SIGmoidal' 
    elif dataset=='seed':
        q = 8
        pa = 0.9
        pk = 0.9
        pm = 0.9
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'LOGarithmic'
    elif dataset=='synthetic':
        q = 8
        pa = 0.9
        pk = 0.9
        pm = 0.9
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'SIGmoidal' 
    elif dataset=='thyroid':
        q = 10
        pa = 0.9
        pk = 0.9
        pm = 0.9
        alpha_type = 'SOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'Essential' 
    elif dataset=='wine':
        q = 8
        pa = 0.9
        pk = 0.9
        pm = 0.9
        alpha_type = 'PLOWA'  # 'PLOWA' , 'SOWA'
        loss_type = 'LOG-Linear'  

    return k, t_max, Restarts, fuzzy_degree, q, pa, pk , pm, alpha_type, loss_type
