import _matrix
import cpp_dis
import py_dis
import random
import time

if __name__ == '__main__':
	
	runs = 10000
	
	
	
	cpp_s_time = time.time()
	
	for i in range(runs):
		A = _matrix.Matrix(1, 1024)
		B = _matrix.Matrix(1, 1024)
		
		for j in range(1024):
			A[1, j] = random.randint(-4096, 4096) / 1024
			B[1, j] = random.randint(-4096, 4096) / 1024
		
		dis = cpp_dis.euclidean(A, B)
		
	cpp_e_time = time.time()
	
	cpp_time = cpp_e_time - cpp_s_time
	
	
	
	
	py_s_time = time.time()
	
	for i in range(runs):
		A = _matrix.Matrix(1, 1024)
		B = _matrix.Matrix(1, 1024)
		
		for j in range(1024):
			A[1, j] = random.randint(-4096, 4096) / 1024
			B[1, j] = random.randint(-4096, 4096) / 1024
		
		dis = py_dis.euclidean(A, B)
	
	py_e_time = time.time()
	
	py_time = py_e_time - py_s_time
	
	
	
	print("py_time / cpp_time = {}".format(float(py_time / cpp_time)))
	
	
