import matrix
import cpp_dis
import py_dis
import random
import time

if __name__ == '__main__':

    runs = 10
    vlen = 16
    A = matrix.Matrix(vlen, 1)
    B = matrix.Matrix(vlen, 1)
    print("doing cpp")
    cpp_s_time = time.time()

    for i in range(runs):

        for j in range(vlen):
            A[j, 0] = random.randint(-4096, 4096) / 1024
#            print(A[j, 0])
            B[j, 0] = random.randint(-4096, 4096) / 1024
#            print(B[j, 0])

        dis = cpp_dis.euclidean(A, B)

    cpp_e_time = time.time()
    cpp_time = cpp_e_time - cpp_s_time
    print("doing mkl")
    mkl_s_time = time.time()

    for i in range(runs):
        for j in range(vlen):
            A[j, 0] = random.randint(-4096, 4096) / 1024
#            print(A[j, 0])
            B[j, 0] = random.randint(-4096, 4096) / 1024
#            print(B[j, 0])
        dis = cpp_dis.mkl_euclidean(A, B)

    mkl_e_time = time.time()
    mkl_time = mkl_e_time - mkl_s_time
    print("cpp_time / mkl_time = {}".format(float(cpp_time / mkl_time)))
    print("done")

