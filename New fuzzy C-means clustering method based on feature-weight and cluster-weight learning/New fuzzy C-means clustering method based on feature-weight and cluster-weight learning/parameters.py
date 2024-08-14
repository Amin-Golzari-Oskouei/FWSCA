def parameters(dataset, lable_true, col, data):

    import numpy as np

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree
    p_init = 0                   # initial p.
    p_max = 0.5                  # maximum p.
    p_step = 0.01                # p step.

    # specific parameters
    if dataset=='iris':
        q = 2                        # the value for the feature weight updates.
        beta_memory = 0.3            # amount of memory for the cluster weight updates.
        l = 1                        # i must take a value in (0,1]
    elif dataset=='balance':
        q = 4                        # the value for the feature weight updates.
        beta_memory = 0.2            # amount of memory for the cluster weight updates.
        l = 0.0001  
    elif dataset=='breast':
        q = -2                       # the value for the feature weight updates.
        beta_memory = 0.3            # amount of memory for the cluster weight updates.
        l = 0.1  
    elif dataset=='bupa':
        q = -4                       # the value for the feature weight updates.
        beta_memory = 0.3            # amount of memory for the cluster weight updates.
        l = 1 
    elif dataset=='cancer':
        q = -2                       # the value for the feature weight updates.
        beta_memory = 0.             # amount of memory for the cluster weight updates.
        l = 0.1 
    elif dataset=='zoo':
        q = 6                        # the value for the feature weight updates.
        beta_memory = 0.3            # amount of memory for the cluster weight updates.
        l = 0.1 
    elif dataset=='dermatology':
        q = 4                        # the value for the feature weight updates.
        beta_memory = 0.1            # amount of memory for the cluster weight updates.
        l = 0.0001 
    elif dataset=='diabet':
        q = -2                        # the value for the feature weight updates.
        beta_memory = 0.            # amount of memory for the cluster weight updates.
        l = 0.0001 
    elif dataset=='ecoli':
        q = -10                        # the value for the feature weight updates.
        beta_memory = 0.2            # amount of memory for the cluster weight updates.
        l = 1 
    elif dataset=='glass':
        q = -8                        # the value for the feature weight updates.
        beta_memory = 0.2            # amount of memory for the cluster weight updates.
        l = 0.0001 
    elif dataset=='wine':
        q = -4                        # the value for the feature weight updates.
        beta_memory = 0.3            # amount of memory for the cluster weight updates.
        l = 0.1 
    elif dataset=='thyroid':
        q = -6                        # the value for the feature weight updates.
        beta_memory = 0.0            # amount of memory for the cluster weight updates.
        l = 0.01 
    elif dataset=='synthetic':
        q = -8                        # the value for the feature weight updates.
        beta_memory = 0.0            # amount of memory for the cluster weight updates.
        l = 0.1 
    elif dataset=='spectfheart':
        q = -2                        # the value for the feature weight updates.
        beta_memory = 0.1            # amount of memory for the cluster weight updates.
        l = 0.1 
    elif dataset=='letters':
        q = 2                        # the value for the feature weight updates.
        beta_memory = 0.3            # amount of memory for the cluster weight updates.
        l = 1 
    elif dataset=='ionosphere':
        q = 2                        # the value for the feature weight updates.
        beta_memory = 0.2            # amount of memory for the cluster weight updates.
        l = 0.0001 
    elif dataset=='heberman':
        q = 2                        # the value for the feature weight updates.
        beta_memory = 0.1            # amount of memory for the cluster weight updates.
        l = 0.0001 
    elif dataset=='heart':
        q = -4                        # the value for the feature weight updates.
        beta_memory = 0.1            # amount of memory for the cluster weight updates.
        l = 0.1 
    elif dataset=='seed':
        q = -2                        # the value for the feature weight updates.
        beta_memory = 0.1            # amount of memory for the cluster weight updates.
        l = 0.1 
    elif dataset=='Car_evaluation':
        q = -2                        # the value for the feature weight updates.
        beta_memory = 0.1            # amount of memory for the cluster weight updates.
        l = 0.1 
    elif dataset=='soybean':
        q = -10                        # the value for the feature weight updates.
        beta_memory = 0.1            # amount of memory for the cluster weight updates.
        l = 0.0001 
    elif dataset=='breast_tissue':
        q = 10                        # the value for the feature weight updates.
        beta_memory = 0.3            # amount of memory for the cluster weight updates.
        l = 1     
    elif dataset=='cmc':
        q = -10                        # the value for the feature weight updates.
        beta_memory = 0.2            # amount of memory for the cluster weight updates.
        l = 1 
    elif dataset=='waveform':
        q = 2                        # the value for the feature weight updates.
        beta_memory = 0.0            # amount of memory for the cluster weight updates.
        l = 0.0001 
    elif dataset=='synthetic_global':
        q = 10                        # the value for the feature weight updates.
        beta_memory = 0.0            # amount of memory for the cluster weight updates.
        l = 0.01 
    elif dataset=='vowel':
        q = 6                       # the value for the feature weight updates.
        beta_memory = 0.3            # amount of memory for the cluster weight updates.
        l = 0.0001 
    
    
    
    landa = np.zeros(col)
    landa = l/np.var(data, 0)
    landa[np.where(np.isinf(landa))] = 1
        
    return k, t_max, Restarts, fuzzy_degree, q, p_init, p_max, p_step, beta_memory, landa