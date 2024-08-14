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
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='breast':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='bupa':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='cmc':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='coil2':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='dermatology':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='ecoli':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='fertility':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='glass':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='seed':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='seismic':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='zoo':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='wine':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='vowel':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='thyroid':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='soybean':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='cmc':
        A = 2.1                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='synthetic_global':
        A = 2.6                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='waveform':
        A = 2.1                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='vowel':
        A = 4.6                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    elif dataset=='breast_tissue':
        A = 10                     # the exponent value for the feature weight updates (β parameter in the original Paper).
    return k, t_max, Restarts, fuzzy_degree, A