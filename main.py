from matrix_methods import c_sum, c_mult, c_det
res = c_sum([[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]])
res1 = c_mult([[1,0,0],[0,1,0], [0,0,1]],[[1,2,3],[4,5,6], [1,2,3]])
res2 = c_det([[51,1,65,0,0],[0,2,0,0,0], [0,5,7,0,0],[0,0,0,5,0],[0,0,0,0,1]])
print(res)
print(res1)
print(res2)