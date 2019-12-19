#include <cmath>
#include <mkl.h>
#include "matrix.cpp"
#include <iostream>
using namespace std;

// Sum of Absolute Differnces
float sad(Matrix const & A, Matrix const & B){
	
	size_t row = A.nrow();
	float res = 0;

	// setting the matrix to 0
	for(size_t i = 0; i < row; ++i){
		float mid_res = A(i, 0) - B(i, 0);
		
		// absolute
		if (mid_res < 0) res += -mid_res;
		else res += mid_res;
	}
	
	return res;
}

// Sum of Squared Differnces
float ssd(Matrix const & A, Matrix const & B){
	
	size_t row = A.nrow();
	float res = 0;

	// setting the matrix to 0
	for(size_t i = 0; i < row; ++i){
		float mid_res = A(i, 0) - B(i, 0);
		
		// squared
		res += mid_res * mid_res;
	}
	
	return res;
}

// Mean-Absolute Error
float mae(Matrix const & A, Matrix const & B){
	
	size_t row = A.nrow();
	
	float res = 0;

	// setting the matrix to 0
	for(size_t i = 0; i < row; ++i){
		float mid_res = A(i, 0) - B(i, 0);
		
		// absolute
		if (mid_res < 0) res += -mid_res;
		else res += mid_res;
	}
	
	return res / row;
}

// Euclidean
float euclidean(Matrix const & A, Matrix const & B){
	return sqrt(ssd(A, B));
}


float mkl_euclidean(Matrix const & A, Matrix const & B){
	int v_size = A.ncol() * A.nrow();
	mkl_set_num_threads(1);
	double* res_vec = new double(v_size);
	vdSub(v_size, A.m_buffer, B.m_buffer, res_vec);
	double res = cblas_dnrm2(v_size, res_vec, 1);
	cout << res << endl;
	cout << res_vec << endl;
	if(res_vec) {delete[] res_vec;}
	cout << res_vec << endl;
	return (float)res;
}

float mkl_sad(Matrix const & A, Matrix const & B){
	int v_size = A.ncol() * A.nrow();
	mkl_set_num_threads(1);
	double* res_vec = new double(v_size);
	vdAbs(v_size, A.m_buffer, res_vec);
	double res = cblas_dnrm2(v_size, res_vec, 1);
	cout << res << endl;
	cout << res_vec << endl;
	if(res_vec) {delete[] res_vec;}
	cout << res_vec << endl;
	return (float)res;
}

PYBIND11_MODULE(cpp_dis, m) {
  m.def("sad", &sad, "Sum of Absolute Differnces");
  m.def("ssd", &ssd, "Sum of Squared Differnces");
  m.def("mae", &mae, "Mean-Absolute Error");
  m.def("euclidean", &euclidean, "Euclidean");
  m.def("mkl_euclidean", &mkl_euclidean, "Euclidean using cblas");
  m.def("mkl_sad", &mkl_sad, "SAD using cblas");
}

