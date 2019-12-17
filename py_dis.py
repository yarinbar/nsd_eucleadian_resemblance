import numpy as np


def euclidean(a, b):
    return np.linalg.norm(a - b)


def sad(q, a, b):
    
    dqa = np.sum(np.absolute(q - a))
    dqb = np.sum(np.absolute(q - b))
    
    if dqa < dqb:
        return 0
    
    return 1
