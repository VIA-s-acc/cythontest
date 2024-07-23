#include <stdlib.h>

void multiply_matrices(double* matrix_a, double* matrix_b, double* result_matrix, int rows_a, int cols_a, int rows_b, int cols_b) {
    for (int i = 0; i < rows_a; ++i) {
        for (int j = 0; j < cols_b; ++j) {
            result_matrix[i * cols_b + j] = 0;
            for (int k = 0; k < cols_a; ++k) {
                result_matrix[i * cols_b + j] += matrix_a[i * cols_a + k] * matrix_b[k * cols_b + j];
            }
        }
    }
}

void sum_matrices(double* matrix_a, double* matrix_b, double* result_matrix, int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result_matrix[i * cols + j] = matrix_a[i * cols + j] + matrix_b[i * cols + j];
        }
    }
}


double det(double* matrix, int rows, int cols) {

    double determinant = 1;
    for (int i = 0; i < rows; ++i) {
        for (int j = i + 1; j < rows; ++j) {
            double factor = matrix[j * cols + i] / matrix[i * cols + i];
            for (int k = i; k < cols; ++k) {
                matrix[j * cols + k] -= factor * matrix[i * cols + k];
            }
        }
        determinant *= matrix[i * cols + i];
    }

    return determinant;
}
