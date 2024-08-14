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

        elif dataset=='breast':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='bupa':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='cancer':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function

        elif dataset=='dermatology':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='diabet':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='ecoli':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='glass':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='heberman':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='ionosphere':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function

        elif dataset=='letters':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='seed':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='synthetic':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='spectfheart':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function

        elif dataset=='wine':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='thyroid':
                a_coefficient = 1;           # coefficient of u
                b_coefficient = 1;           # coefficient of t
                balance_tarm = 1;            # balance parameter among to terms of loss function
        elif dataset=='cmc':
                a_coefficient = 1.9;           # coefficient of u
                b_coefficient = 3.1;           # coefficient of t
                balance_tarm = 1.1;            # balance parameter among to terms of loss function
        elif dataset=='synthetic_global':
                a_coefficient = 1.5;           # coefficient of u
                b_coefficient = 2.9;           # coefficient of t
                balance_tarm = 2.6;            # balance parameter among to terms of loss function
        elif dataset=='vowel':
                a_coefficient = 0.3;           # coefficient of u
                b_coefficient = 0.7;           # coefficient of t
                balance_tarm = 4.6;            # balance parameter among to terms of loss function
        elif dataset=='breast_tissue':
                a_coefficient = 0.5;           # coefficient of u
                b_coefficient = 0.5;           # coefficient of t
                balance_tarm = 1.6;            # balance parameter among to terms of loss function
        elif dataset=='waveform':
                a_coefficient = 3.9;           # coefficient of u
                b_coefficient = 3.7;           # coefficient of t
                balance_tarm = 4.1;            # balance parameter among to terms of loss function
    
        
        return k, t_max, Restarts, fuzzy_degree, T_pow, a_coefficient, b_coefficient, balance_tarm
