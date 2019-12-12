import numpy as np


def euclidean(q, a, b):
    
    dqa = np.linalg.norm(q - a)
    dqb = np.linalg.norm(q - b)
    
    if dqa < dqb:
        return 0
    
    return 1


def sad(q, a, b):
    
    dqa = np.sum(np.absolute(q - a))
    dqb = np.sum(np.absolute(q - b))
    
    if dqa < dqb:
        return 0
    
    return 1
