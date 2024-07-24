Example of Cython using


# Comparison of the speed of code for matrix multiplication in standard Python and with Cython

## C Code
- [.c file](matrix_methods/lowlevel/matr_m.c)
- [.pyx file](matrix_methods/matr_mult.pyx)

## Python Code
- [.py file line 5:11](matrix_methods/perf.py)

## Matrices for comparison
![Matrix](media/matrix.png)

## Comparison results
```bash
Elapsed time: 2.135 | type: Cython
Elapsed time: 165.009 | type: Python

Cython is faster than Python ~ about 77 times ( in this case )

```

![Comparison](media/cy_py.png)

#### Averages:
-----
```go
matrix sizes 521 x 241 and 241 x 652 | num_iterations = 100 

Average cython time: 0.1339475417137146
Average cython time: 9.9339475417137146
```


#### Table:
---

| Matrix A Size | Matrix B Size | Operation    | Iterations | Cython               | Python                |
| ------------- | ------------- | :--------    | ---------- | ------               | ------                |
| 521 x 241     | 241 x 652     |  Multiply    | 100        |0.134 sec             | 9.934   sec           |
| 2500 x 250    | 250 x 2500    |  Multiply    | 1          |2.135 sec             | 165.009 sec           |
| 1000 x 1000   | None          |  Determinant | 1          |0.315 sec             | 33.747  sec           |
| 2000 x 2000   | None          |  Determinant | 1          |2.603 sec             | 271.484 sec           |

[.csv file](table.csv)