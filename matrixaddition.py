import numpy as np
x = 3
y = 4
z = 1
mat1 = np.random.randint(100, size=(x,y))
mat2 = np.random.randint(100, size = (y,z))
matrix = np.array([[0 for x in range(z)] for y in range(x)])
print("matrix 1:")
print(mat1)
print("matrix 2:")
print(mat2)
for i in range(3):
    for j in range(1):
        for k in range(4):
            matrix[i,j] += mat1[i,k]*mat2[k,j]

       
print("Product of matrix 1 and 2:")
print(matrix)



