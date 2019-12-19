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
		

def convert_to_np(A):
    arr = []
    for i in range(A.nrow):
        arr.append(A[i, 0])
    return np.array(arr)

def np_euclidean(A, B):
	if type(A)is not np.ndarray:
		A = convert_to_np(A)
		
	if type(B)is not np.ndarray:
		A = convert_to_np(B)
		
	return np.linalg.norm(np.absolute(A - B))
	

def np_sad(A, B):
	if type(A) is not np.ndarray:
		A = convert_to_np(A)
		
	if type(B)is not np.ndarray:
		A = convert_to_np(B)

	return np.sum(np.abs.np.subtract(A, B))
	
