"""   Joining & Split NumPy   """
import numpy as np

# Join Array

var = np.array([1, 2, 3, 4])
var1 = np.array([9, 8, 7, 6])

con = np.concatenate((var, var1))
print(con)  # [1 2 3 4 9 8 7 6]

vr = np.array([[1, 2], [3, 4]])
vr1 = np.array([[9, 8], [7, 6]])
con0 = np.concatenate((vr, vr1), axis=0)
con1 = np.concatenate((vr, vr1), axis=1)
print(con0)
print(con1)
"""
Output:

axis = 0 / Row-wise ---------------------
[[1 2]
 [3 4]
 [9 8]
 [7 6]]

Axis = 1 / Column-wise-----------------------
[[1 2 9 8]
 [3 4 7 6]]
"""

stack = np.hstack((var, var1))  # Row  [1 2 3 4 9 8 7 6]

stack = np.vstack(
    (var, var1)
)  # Column == axis=0 or default == np.stack((var,var1),axis=0)
# [[1 2 3 4]
#  [9 8 7 6]]
stack = np.dstack((var, var1))  # == np.stack((var,var1),axis=1)
# [[[1 9]
#   [2 8]
#   [3 7]
#   [4 6]]]

print(stack)
print()
""" Spliting """

sp = np.split(var, 2)  # [array([1, 2]), array([3, 4])]
print(sp)
print(type(sp))  # <class 'list'>


arr_sp = np.array_split(var, 2)
print(arr_sp)
print(type(arr_sp))
# If you want very array
print(arr_sp[0])  # [1 2]
print(type(arr_sp[0]))  # <class 'numpy.ndarray'>


# Move on to 2 dimension Array
var_2dim = np.array([[1, 2, 3], [1, 2, 3]])

print(var_2dim)
arr_sp_2dim = np.array_split(var_2dim, 3,axis=1)
print(arr_sp_2dim)