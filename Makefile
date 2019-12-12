
CXX := g++
FLAGS ?= -std=c++17 -O3 -g -m64 -Wall -shared -fPIC
FILE1 = matrix.cpp
SUFFIX = $(shell python3-config --extension-suffix)
TARGET2 = _matrix$(SUFFIX)

FILE2 = cpp_dis.cpp
TARGET2 = _cpp_dis$(SUFFIX)

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
all: $(TARGET)

$(TARGET1): $(FILE1)
	$(CXX) $(FLAGS) $(INCLUDES) $^ -o $@ $(LDFLAGS)

$(TARGET2): $(FILE2)
	$(CXX) $(FLAGS) $(INCLUDES) $^ -o $@ $(LDFLAGS)

.PHONY: clean
clean:
	rm -f *.so
