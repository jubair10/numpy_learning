"""     Indexing and Slicing    """
import numpy as np

# Indexing
var = np.array([9, 8, 7, 6])
#               0  1  2  3
# print(var[-4])

var1 = np.array([[9, 8, 7], [4, 5, 6]])
print(var1[0])


var2 = np.array([[[9, 8, 7], [4, 5, 6]]])

# [ (0) [ (0) [9 8 7]
#              [4 5 6] (1) ] (1) ]
print(var2)
print(var2[0, 1, 0])  # == 4

# Slicing is similar to list, string
print(var[:])
