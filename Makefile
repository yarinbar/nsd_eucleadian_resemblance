
CXX := g++
FLAGS ?= -std=c++17 -O3 -g -m64 -Wall -shared -fPIC
MATRIX = matrix.cpp
SUFFIX = $(shell python3-config --extension-suffix)
MATRIX_TARGET = matrix$(SUFFIX)

DISTANCE = cpp_dis.cpp
DISTANCE_TARGET = cpp_dis$(SUFFIX)

MKLPATH ?= ${HOME}/opt/conda
INCLUDES += -m64 -I${MKLPATH}/include \
	${MKLPATH}/lib/libmkl_intel_thread.so \
	${MKLPATH}/lib/libmkl_intel_lp64.so \
	${MKLPATH}/lib/libmkl_sequential.so \
	${MKLPATH}/lib/libmkl_avx2.so \
	${MKLPATH}/lib/libmkl_def.so \
	${MKLPATH}/lib/libmkl_core.so

LDFLAGS += -L${MKLPATH}/lib -Wl,--no-as-needed \
	-lmkl_rt -lpthread -lm -ldl

INCLUDES += `python -m pybind11 --includes`
CXXFLAGS += -shared -fPIC

.PHONY: all
all: $(MATRIX_TARGET) $(DISTANCE_TARGET)

$(MATRIX_TARGET): $(MATRIX)
	$(CXX) $(FLAGS) $(INCLUDES) $^ -o $@ $(LDFLAGS)

$(DISTANCE_TARGET): $(DISTANCE)
	$(CXX) $(FLAGS) $(INCLUDES) $^ -o $@ $(LDFLAGS)

.PHONY: clean
clean:
	rm -f *.so

.PHONY: bench
bench:
	python3 bench.py
	
.PHONY: test_dis
test_dis:
	pytest -sv validate.py
	
