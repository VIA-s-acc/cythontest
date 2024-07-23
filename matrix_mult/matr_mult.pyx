from libc.stdlib cimport malloc, free

cdef extern from "lowlevel\matr_m.c":
    void multiply_matrices(double* matrix_a, double* matrix_b, double* result_matrix, int rows_a, int cols_a, int rows_b, int cols_b)

def multiply_matrices_wrapper(matrix_a, matrix_b):
    cdef int rows_a = len(matrix_a)
    cdef int cols_a = len(matrix_a[0])
    cdef int rows_b = len(matrix_b)
    cdef int cols_b = len(matrix_b[0])
    
    cdef int size_a = rows_a * cols_a
    cdef int size_b = rows_b * cols_b
    cdef int size_result = rows_a * cols_b
    
    cdef double* c_matrix_a = <double*>malloc(size_a * sizeof(double))
    cdef double* c_matrix_b = <double*>malloc(size_b * sizeof(double))
    cdef double* result_matrix = <double*>malloc(size_result * sizeof(double))
    
    for i in range(rows_a):
        for j in range(cols_a):
            c_matrix_a[i * cols_a + j] = matrix_a[i][j]

    for i in range(rows_b):
        for j in range(cols_b):
            c_matrix_b[i * cols_b + j] = matrix_b[i][j]

    multiply_matrices(c_matrix_a, c_matrix_b, result_matrix, rows_a, cols_a, rows_b, cols_b)
    
    result = [[result_matrix[i * cols_b + j] for j in range(cols_b)] for i in range(rows_a)]
    
    free(c_matrix_a)
    free(c_matrix_b)
    free(result_matrix)
    
    return result
