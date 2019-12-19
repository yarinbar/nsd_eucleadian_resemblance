import matrix

import cpp_dis
import py_dis

import numpy as np
import random

import unittest


class TestDis(unittest.TestCase):
    def create_random(self, rows, cols):
        A = matrix.Matrix(rows, cols)
        for i in range(rows):
            for j in range(cols):
                A[i, j] = random.randint(0, 100)
        return A

    def create_zero(self, rows, cols):
        A = matrix.Matrix(rows, cols)
        for i in range(rows):
            for j in range(cols):
                A[i, j] = 0
        return A

    def convert_to_np(self, A):
        arr = []
        for i in range(A.nrow):
            arr.append(A[i, 0])
        return np.array(arr)

    def test_euclidean_zero(self):

        zero = self.create_zero(1024, 1)

        self.assertEqual(cpp_dis.euclidean(zero, zero), 0)
        self.assertEqual(cpp_dis.mkl_euclidean(zero, zero), 0)
        self.assertEqual(py_dis.euclidean(zero, zero), 0)

    def test_sad_zero(self):

        zero = self.create_zero(1024, 1)

        self.assertEqual(cpp_dis.sad(zero, zero), 0)
        self.assertEqual(cpp_dis.mkl_sad(zero, zero), 0)
        self.assertEqual(py_dis.sad(zero, zero), 0)

    def test_euclidean(self):
        runs = 1000

        for i in range(runs):
            vec1 = self.create_random(1024, 1)
            vec2 = self.create_random(1024, 1)
            np_vec1 = self.convert_to_np(vec1)
            np_vec2 = self.convert_to_np(vec2)

            res = np.linalg.norm(np_vec1 - np_vec2)

            mkl_res = cpp_dis.mkl_euclidean(vec1, vec2)
            cpp_res = cpp_dis.euclidean(vec1, vec2)
            py_res  = py_dis.euclidean(vec1, vec2)

            self.assertAlmostEqual(res, mkl_res, 3)
            self.assertAlmostEqual(res, cpp_res, 3)
            self.assertAlmostEqual(res, py_res, 3)

    def test_sad(self):
        runs = 1000

        for i in range(runs):
            vec1 = self.create_random(1024, 1)
            vec2 = self.create_random(1024, 1)

            np_vec1 = self.convert_to_np(vec1)
            np_vec2 = self.convert_to_np(vec2)
            res = np.linalg.norm(np_vec1 - np_vec2)

            mkl_res = cpp_dis.mkl_euclidean(vec1, vec2)
            cpp_res = cpp_dis.euclidean(vec1, vec2)
            py_res  = py_dis.euclidean(vec1, vec2)

            self.assertAlmostEqual(res, mkl_res, 3)
            self.assertAlmostEqual(res, cpp_res, 3)
            self.assertAlmostEqual(res, py_res, 3)

