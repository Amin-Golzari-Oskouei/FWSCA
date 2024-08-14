def parameters(dataset, lable_true, col, data):

    import numpy as np

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree

    # specific parameters
    if dataset=='iris':
        landa = 1.4 
    elif dataset=='balance':
        landa = 0.2 
    elif dataset=='breast':
        landa = 0.1
    elif dataset=='bupa':
        landa = 5.0 
    elif dataset=='cancer':
        landa = 0.1 
    elif dataset=='Car_evaluation':
        landa = 0.6 
    elif dataset=='dermatology':
        landa = 1.0 
    elif dataset=='diabet':
        landa = 0.1 
    elif dataset=='ecoli':
        landa = 1.0 
    elif dataset=='glass':
        landa = 1.0
    elif dataset=='heberman':
        landa = 3.0
    elif dataset=='ionosphere':
        landa = 0.1
    elif dataset=='heart':
        landa = 1.0   
    elif dataset=='letters':
        landa = 0.1 
    elif dataset=='zoo':
        landa = 1.0 
    elif dataset=='wine':
        landa = 0.1 
    elif dataset=='seed':
        landa = 0.1 
    elif dataset=='thyroid':
        landa = 0.5 
    elif dataset=='soybean':
        landa = 0.2 
    elif dataset=='synthetic':
        landa = 0.1 
    elif dataset=='spectfheart':
        landa = 0.1  
    elif dataset=='cmc':
        landa = 1.4 
    elif dataset=='vowel':
        landa = 0.1 
    elif dataset=='waveform':
        landa = 0.4 
    elif dataset=='synthetic_global':
        landa = 0.2 
    elif dataset=='Image_Segmentation':
        landa = 0.1 
        
    return k, t_max, Restarts, fuzzy_degree, landa

