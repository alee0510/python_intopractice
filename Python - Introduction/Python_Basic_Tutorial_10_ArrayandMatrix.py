# tutorial 10 : array and matrix
from numpy import zeros, mat, transpose, array

print("Tutorial 10 : Array and Matrix\n")

# define an array
print("Array")
h = zeros(4)                # define an aray with 4 components with 0 value for each components
h[0] = 1
h[1] = 2
h[2] = 3
h[3] = 4                    # index start by 0 end with 3
print("h = ", h)

# define a matrix
print("\nMatrix")
x = array([[1, 2], [3, 4]])
m = mat(x)                  # define a matrix
t = transpose(m)

print("matrix 2x2\n", m)
print("transpose\n", t)

# matrix identity
print()
i = zeros((2, 2))
i = mat(i)
i[0, 0] = 1; i[0, 1] = 0
i[1, 0] =0 ; i[1, 1] = 1
print("identity matrix\n", i)

# matrix operation
print("multiply\n", t*m)

# matrix using for loop
A = zeros((2,2))
A = mat(A)
n = 0
for i in range(0, 2):
    for j in range(0, 2):
        A[i, j] = n
        n += 1

print("using for loop\n", A)