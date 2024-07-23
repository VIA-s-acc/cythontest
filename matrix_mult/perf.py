from time import time 
from build.matr_mult import multiply_matrices_wrapper
import random

def matmult(a, b):
    if len(a[0]) != len(b):
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
                
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
    



