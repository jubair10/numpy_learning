"""    Matrix Numpy Arrays    """
import numpy as np

var = np.matrix([[1, 2, ], [1, 2, ]])
print(var)
print(type(var))

var2 = np.matrix([[1, 2, ], [1, 2, ]])
print(var2)
# print(var+var2)
# print(var-var2)
# print(var/var2)

# Multiplication in Matrix is called DOT Multiplication
print("Matrix Multiplication: ",)
print(var.dot(var2))


print()
var1=np.array([[1, 2, 3], [1, 2, 3]])
print(var1)
print(type(var1))

