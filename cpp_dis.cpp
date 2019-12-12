#include <cmath>
#include <matrix.cpp>


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



PYBIND11_MODULE(_cpp_dis, m) {
  
  m.def("sad", &sad, "Sum of Absolute Differnces");
  m.def("ssd", &ssd, "Sum of Squared Differnces");
  m.def("mae", &mae, "Mean-Absolute Error");
  m.def("euclidean", &euclidean, "Euclidean");
  
}

