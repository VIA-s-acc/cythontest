from time import time 
from build.matr_mult import multiply_matrices_wrapper
import random

def matmult(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def c_mult(matrix_a, matrix_b):
    result = multiply_matrices_wrapper(matrix_a, matrix_b)
    return result

def performance(f, type = "C"):
    def handler(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        end = time()
        handler.resultString = (f'Elapsed time: {(end - start):.3f} | type: {type}')
        
    handler.resultString = None
    return handler


if __name__ == "__main__":
    rows_a, cols_a = 250, 200
    rows_b, cols_b = 200, 250
    matrix_a = [[random.random() for _ in range(cols_a)] for _ in range(rows_a)]
    matrix_b = [[random.random() for _ in range(cols_b)] for _ in range(rows_b)]

    
    c_func = performance(c_mult, type="Cython")
    p_func = performance(matmult, type="Python")
    c_func(matrix_a, matrix_b)
    print(c_func.resultString)
    p_func(matrix_a, matrix_b)
    print(p_func.resultString)



