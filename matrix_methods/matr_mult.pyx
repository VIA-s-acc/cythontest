from libc.stdlib cimport malloc, free

cdef extern from "lowlevel\matr_m.c" nogil:
    void multiply_matrices(double* matrix_a, double* matrix_b, double* result_matrix, int rows_a, int cols_a, int rows_b, int cols_b)
    void sum_matrices(double* matrix_a, double* matrix_b, double* result_matrix, int rows, int cols) 
    double det(double* matrix, int rows, int cols) 


def determinant(matrix_a):
    
    cdef int rows_a = len(matrix_a)
    cdef int cols_a = len(matrix_a[0])

    cdef int size_a = rows_a * cols_a 
    cdef double* c_matrix_a = <double*>malloc(size_a * sizeof(double))
    for i in range(rows_a):
        for j in range(cols_a):
            c_matrix_a[i * cols_a + j] = matrix_a[i][j]
    cdef double result = 0

    result = det(c_matrix_a, rows_a, cols_a)

    free(c_matrix_a)
    
    return result

def sum_matrices_wrapper(matrix_a, matrix_b):
    
    """
    This module provides a wrapper function for summing two matrices using a C implementation.

    Parameters:
        matrix_a (List[List[float]]): The first matrix to sum.
        matrix_b (List[List[float]]): The second matrix to sum.

    Returns:
        List[List[float]]: The sum of the two matrices.

    Example:
        >>> matrix_a = [[1, 2], [3, 4]]
        >>> matrix_b = [[5, 6], [7, 8]]
        >>> sum_matrices_wrapper(matrix_a, matrix_b)
        [[6, 8], [10, 12]]

    """


    cdef int rows_a = len(matrix_a)
    cdef int cols_a = len(matrix_a[0])
    
    cdef int size_a = rows_a * cols_a
    
    cdef double* c_matrix_a = <double*>malloc(size_a * sizeof(double))
    cdef double* c_matrix_b = <double*>malloc(size_a * sizeof(double))
    cdef double* result_matrix = <double*>malloc(size_a * sizeof(double))
    
    for i in range(rows_a):
        for j in range(cols_a):
            c_matrix_a[i * cols_a + j] = matrix_a[i][j]
            c_matrix_b[i * cols_a + j] = matrix_b[i][j]



    sum_matrices(c_matrix_a, c_matrix_b, result_matrix, rows_a, cols_a)
    
    result = [[result_matrix[i * cols_a + j] for j in range(cols_a)] for i in range(rows_a)]
    
    free(c_matrix_a)
    free(c_matrix_b)
    free(result_matrix)
    
    return result


def multiply_matrices_wrapper(matrix_a, matrix_b):
        
    """
    This module provides a wrapper function for multiplying two matrices using a C implementation.

    Parameters:
        matrix_a (List[List[float]]): The first matrix to multiply.
        matrix_b (List[List[float]]): The second matrix to multiply.

    Returns:
        List[List[float]]: The result of the matrix multiplication.

    Example:
        >>> matrix_a = [[1, 2], [3, 4]]
        >>> matrix_b = [[5, 6], [7, 8]]
        >>> multiply_matrices_wrapper(matrix_a, matrix_b)
        [[19, 22], [43, 50]]

    """
    
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
