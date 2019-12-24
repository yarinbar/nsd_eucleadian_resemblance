
import py_dis
import cpp_dis
import numpy as np
import os

from model import FVModel
from dataset import Dataset

def my_pred_func(q, a, b):
	dqa = py_dis.np_euclidean(q, a)
	dqb = py_dis.np_euclidean(q, b)
	
	if dqa < dqb:
		return 0
	
	return 1

if __name__ == '__main__':
	
	my_model = FVModel(my_pred_func)
	
	ds_path = os.path.join(path.dirname(__file__), 'data')
	
	dataset  = Dataset(ds_path)
	
	print(my_model.test(dataset.X, dataset.y_true))
	