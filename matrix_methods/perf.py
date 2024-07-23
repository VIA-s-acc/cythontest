from time import time 
from .build.matr_mult import multiply_matrices_wrapper, sum_matrices_wrapper, determinant
import random
from math import isnan
from copy import deepcopy
def c_det(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix must be square")
    res = determinant(matrix)
    if isnan(res):
        raise ValueError("NaN value")
    return res     

def matmult(a, b):
    if len(a[0]) != len(b):
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
                
    return result

def c_sum(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b[0]) and len(matrix_a) != len(matrix_b):
        raise(ValueError("The shape of the matrices must be the same"))
    
    result = sum_matrices_wrapper(matrix_a, matrix_b)
    
    return result


def c_mult(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
    result = multiply_matrices_wrapper(matrix_a, matrix_b)
    return result

def performance(f, type = "C"):
    def handler(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        end = time()
        handler.resultString = (f'Elapsed time: {(end - start):.3f} | type: {type}')
        handler.resultFloat = end-start
        return res
    handler.resultString = None
    return handler

def deter(matrix):

    A = deepcopy(matrix)
    n = len(A)
    if n != len(A[0]):
        raise ValueError("The matrix must be square.")

    det = 1
    for i in range(n):

        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        det *= A[i][i]

        for k in range(i+1, n):
            if A[i][i] != 0:
                factor = -A[k][i] / A[i][i]
                for j in range(i+1, n):
                    A[k][j] += factor * A[i][j]
    return det

def get_average(f, iterations = 10, rows_a = 521, cols_a = 241, rows_b = 241, cols_b = 652):
    timers = []
    for i in range(iterations):
        matrix_a = [[random.random() for _ in range(cols_a)] for _ in range(rows_a)]
        matrix_b = [[random.random() for _ in range(cols_b)] for _ in range(rows_b)]
        f(matrix_a, matrix_b)
        timers.append(f.resultFloat)
    
    return sum(timers)/len(timers)
        
if __name__ == "__main__":
    rows_a, cols_a = 521, 241
    rows_b, cols_b = 241, 652
    matrix_a = [[random.random() for _ in range(cols_a)] for _ in range(rows_a)]
    matrix_b = [[random.random() for _ in range(cols_b)] for _ in range(rows_b)]


    c_func = performance(c_mult, type="Cython")
    p_func = performance(matmult, type="Python")
    res1 = c_func(matrix_a, matrix_b)
    print(c_func.resultString)
    res2 = p_func(matrix_a, matrix_b)
    print(p_func.resultString)
    num_iterations = 100
    average_c = get_average(c_func, iterations = num_iterations)
    print(f"Average cython time: {average_c} in num_iterations = {num_iterations} |\n matrix sizes {rows_a}x{cols_a} and {rows_b}x{cols_b}")
    average_p = get_average(p_func, iterations = num_iterations)
    print(f"Average python time: {average_p} in num_iterations = {num_iterations} |\n matrix sizes {rows_a}x{cols_a} and {rows_b}x{cols_b}")
    
    matrix = [[random.randint(1,5) if i == j else 0 for i in range(2500)] for j in range(2500)]
    cp_det = performance(c_det)
    p_det = performance(deter, type = 'P')
    res = cp_det(matrix)
    print(cp_det.resultString)
    print(res)
    res1 = p_det(matrix)

    print(p_det.resultString)
    print(res1)
    

