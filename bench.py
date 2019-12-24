import matrix
import cpp_dis
import py_dis
import random
import time
import numpy as np

def convert_to_np(A):
        arr = []
        for i in range(A.nrow):
            arr.append(A[i, 0])
        return np.array(arr)

if __name__ == '__main__':

    runs = 1000
    vlen = 1024
    A = matrix.Matrix(vlen, 1)
    B = matrix.Matrix(vlen, 1)
	
	cpp_time = 0
    mkl_time = 0
	py_time = 0
	npync_time = 0
	npyc_time = 0
	
	print("doing cpp")
    for i in range(runs):

        for j in range(vlen):
            A[j, 0] = random.randint(-4096, 4096) / 128
#            print(A[j, 0])
            B[j, 0] = random.randint(-4096, 4096) / 128
#            print(B[j, 0])
		cpp_s_time = time.time()
        dis = cpp_dis.euclidean(A, B)
		cpp_e_time = time.time()
		cpp_time += cpp_e_time - cpp_s_time
    
	
    print("doing mkl")
    for i in range(runs):
        for j in range(vlen):
            A[j, 0] = random.randint(-4096, 4096) / 128
#            print(A[j, 0])
            B[j, 0] = random.randint(-4096, 4096) / 128
#            print(B[j, 0])
		mkl_s_time = time.time()
        dis = cpp_dis.mkl_euclidean(A, B)
		mkl_e_time = time.time()
		mkl_time += mkl_e_time - mkl_s_time
	
    print("doing py")
    for i in range(runs):
        for j in range(vlen):
            A[j, 0] = random.randint(-4096, 4096) / 128
#            print(A[j, 0])
            B[j, 0] = random.randint(-4096, 4096) / 128
#            print(B[j, 0])
		py_s_time = time.time()
        dis = py_dis.euclidean(A, B)
		py_e_time = time.time()
		py_time += py_e_time - py_s_time

	print("doing numpy no conversion")
	for i in range(runs):
        for j in range(vlen):
            A[j, 0] = random.randint(-4096, 4096) / 128
#            print(A[j, 0])
            B[j, 0] = random.randint(-4096, 4096) / 128
#            print(B[j, 0])
		npync_s_time = time.time()
        dis = py_dis.np_euclidean(A, B)
		npync_e_time = time.time()
		npync_time += npync_e_time - npync_s_time
	
    print("doing numpy conversion")
    for i in range(runs):
        for j in range(vlen):
            A = (np.random.rand(vlen, 1) - 0.5) * 64
#            print(A[j, 0])
            B = (np.random.rand(vlen, 1) - 0.5) * 64
#            print(B[j, 0])
		npyc_s_time = time.time()
        dis = py_dis.np_euclidean(A, B)
		npyc_e_time = time.time()
		npyc_time += npyc_e_time - npyc_s_time
    

    print("mkl_time / cpp_time  = {}".format(float(mkl_time / cpp_time)))
    print("py_time  / cpp_time  = {}".format(float(py_time  / cpp_time)))
    print("npync_time / cpp_time   = {}".format(float(npync_time / cpp_time)))
    print("npyc_time / cpp_time  = {}".format(float(npyc_time / cpp_time)))

    print("done")

