import numpy as np
    
def indices(ns):
    n = np.sum(ns)
    i_ns = np.cumsum(ns)
    
    indices_random = np.random.permutation(np.arange(0, n, 1))
    
    return np.array_split(indices_random, i_ns)[:-1]  