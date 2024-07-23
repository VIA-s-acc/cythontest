Example of Cython using


# Comparison of the speed of code for matrix multiplication in standard Python and with Cython

## C Code
- [.c file](matrix_mult/lowlevel/matr_m.c)
- [.pyx file](matrix_mult/matr_mult.pyx)

## Python Code
- [.py file line 5:11](matrix_mult/perf.py)

## Matrices for comparison
![Matrix](media/matrix.png)

## Comparison results
```bash
Elapsed time: 2.135 | type: Cython
Elapsed time: 165.009 | type: Python

Cython is faster than Python ~ about 77 times ( in this case )
```
![Comparison](media/cy_py.png)

