def parameters(dataset, lable_true):

    # General Parameters
    k = len(set(lable_true))     # number of clusters.
    t_max = 100                  # maximum number of iterations.
    Restarts = 10                # number of FCM restarts.
    fuzzy_degree = 2             # fuzzy membership degree
    T_pow = 2;                   # power of T


    # specific parameters
    if dataset=='waveform':
            a_coefficient = 0.7;           # coefficient of u
            b_coefficient = 1.9;           # coefficient of t
            balance_tarm = 5.1          # balance parameter among to terms of loss function
    elif dataset=='synthetic_global':
        a_coefficient = 0.6;  # coefficient of u
        b_coefficient = 4.6 # coefficient of t
        balance_tarm = 0.6;

    elif dataset=='breast_tissue':
        a_coefficient = 3.1  # coefficient of u
        b_coefficient = 2.5  # coefficient of t
        balance_tarm = 1.1
    elif dataset=='vowel':
        a_coefficient = 0.6 # coefficient of u
        b_coefficient = 4.1 # coefficient of t
        balance_tarm = 1.1
    elif dataset=='cancer':
        a_coefficient = 3.4 # coefficient of u
        b_coefficient = 0.1 # coefficient of t
        balance_tarm = 1.1
    elif dataset=='Car_evaluation':
        a_coefficient = 1.1 # coefficient of u
        b_coefficient = 3.7 # coefficient of t
        balance_tarm = 1.1
    elif dataset=='dermatology':
        a_coefficient = 1 # coefficient of u
        b_coefficient = 1 # coefficient of t
        balance_tarm = 1
    elif dataset=='diabet':
        a_coefficient = 1.9 # coefficient of u
        b_coefficient = 4.0 # coefficient of t
        balance_tarm = 5.1
    elif dataset=='ecoli':
        a_coefficient = 1 # coefficient of u
        b_coefficient = 1 # coefficient of t
        balance_tarm = 1
    elif dataset=='glass':
        a_coefficient = 1.1 # coefficient of u
        b_coefficient = 1.3 # coefficient of t
        balance_tarm = 0.1
    elif dataset=='heberman':
        a_coefficient = 1.3 # coefficient of u
        b_coefficient = 4.9 # coefficient of t
        balance_tarm = 4.6
    elif dataset=='ionosphere':
        a_coefficient = 1.1 # coefficient of u
        b_coefficient = 1.3 # coefficient of t
        balance_tarm = 0.1
    elif dataset=='heart':
        a_coefficient = 0.1 # coefficient of u
        b_coefficient = 1.9 # coefficient of t
        balance_tarm = 1.1
    elif dataset=='letters':
        a_coefficient = 1 # coefficient of u
        b_coefficient = 1 # coefficient of t
        balance_tarm = 1
    elif dataset=='seed':
        a_coefficient = 4.0 # coefficient of u
        b_coefficient = 3.7 # coefficient of t
        balance_tarm = 3.6
    elif dataset=='iris':
        a_coefficient = 0.5 # coefficient of u
        b_coefficient = 2.8 # coefficient of t
        balance_tarm = 2.6
    elif dataset=='synthetic':
        a_coefficient = 3.4 # coefficient of u
        b_coefficient = 0.1 # coefficient of t
        balance_tarm = 1.6
    elif dataset=='spectfheart':
        a_coefficient = 1 # coefficient of u
        b_coefficient = 1 # coefficient of t
        balance_tarm = 1
    elif dataset=='zoo':
        a_coefficient = 1 # coefficient of u
        b_coefficient = 1 # coefficient of t
        balance_tarm = 1
    elif dataset=='wine':
        a_coefficient = 0.1 # coefficient of u
        b_coefficient = 4.9 # coefficient of t
        balance_tarm = 0.1
    elif dataset=='thyroid':
        a_coefficient = 2.5 # coefficient of u
        b_coefficient = 0.1 # coefficient of t
        balance_tarm = 3.1
    elif dataset=='soybean':
        a_coefficient = 3.1 # coefficient of u
        b_coefficient = 0.1 # coefficient of t
        balance_tarm = 3.1

        
    return k, t_max, Restarts, fuzzy_degree, T_pow, a_coefficient, b_coefficient, balance_tarm