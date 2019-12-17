import _cpp_dis
import py_dis
import random
import time

if __name__ == '__main__':
	
	runs = 10000
	
	cpp_s_time = time.time()
	
	for i in range(runs):
		vec_a = random.sample(range(4096), 1024)
		vec_b = random.sample(range(4096), 1024)
		dis = _cpp_dis.euclidean(vec_a, vec_b)
	
	cpp_e_time = time.time()
	
	cpp_time = cpp_e_time - cpp_s_time
	
	py_s_time = time.time()
	
	for i in range(runs):
		vec_a = random.sample(range(4096), 1024)
		vec_b = random.sample(range(4096), 1024)
		dis = py_dis.euclidean(vec_a, vec_b)
	
	py_e_time = time.time()
	
	py_time = py_e_time - py_s_time
	
	print("py_time / cpp_time = {}".format(float(py_time / cpp_time)))
	
	
