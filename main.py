from matrix_methods import c_sum, c_mult
res = c_sum([[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]])
res1 = c_mult([[1,0,0],[0,1,0], [0,0,1]],[[1,2,3],[4,5,6], [1,2,3]])

print(res)
print(res1)