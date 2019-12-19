import numpy as np


def euclidean(A, B):
    row = A.nrow
    res = 0

    for i in range(row):
        mid_res = A[i, 0] - B[i, 0]
        res += mid_res * mid_res
    return np.sqrt(res)


def sad(A, B):
    row = A.nrow
    res = 0

    for i in range(row):
        mid_res = A[i, 0] - B[i, 0]

        if mid_res < 0:
            mid_res = -mid_res

        res += mid_res
        return res
