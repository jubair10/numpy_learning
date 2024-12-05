"""NumPy Arrays Functions"""
import numpy as np

# Search
var = np.array([1, 2, 3, 4, 2, 5, 2, 5, 6, 7])
x = np.where((var % 2) == 0)  # return Index num

print(x)  # (array([1, 4, 6], dtype=int64),)

# Search sorted Array**********
var1 = np.array([x for x in range(10)])
x1 = np.searchsorted(var1, [5, 5], side="right")
print(x1)
print(var1)

# Sort

sort = np.sort(var)
print(sort)

var_str = np.array(["a", "S", "d"])  # ['S' 'a' 'd']
var_str = np.array(["a", "s", "d"])  # ['a' 'd' 's']
print(np.sort(var_str))

# 2d sort

var_2dim = np.array([[1, 10, 3], [5, 1, 8], [1, 5, 8]])
print(np.sort(var_2dim))
"""
[[ 1  3 10]
 [ 1  5  8]
 [ 1  5  8]]
 """


# Filter Array
# Getting some elements out of an existing array and creating a new array out of them
test_array = np.array([1, 2, 3, 4])
f = [True, False, False, True]
filt = test_array[f]  # Elements must be same
print(filt)


""" ---------Part:2--------"""
"""
Arithmetic Function 
>Shuffle
>Unique
>Resize
>Flatten
>Ravel
"""
# >shuffle
s_arr = np.array([1, 2, 3, 4, 5,6])
# np.random.shuffle(s_arr)  # randomly: [1 2 3 5 4]
print(s_arr)

# >Unique
unique = np.unique(
    var, return_index=[True], return_counts=[True], return_inverse=[True]
)
"""
Output:
(array([1, 2, 3, 4, 5, 6, 7]), array([0, 1, 2, 3, 5, 8, 9], dtype=int64), array([0, 1, 2, 3, 1, 4, 1, 4, 5, 6], dtype=int64), array([1, 3, 1, 1, 2, 1, 1], dtype=int64))
"""
print(unique,"\n")

# > Resize is likely Reshape func
resize = np.resize(s_arr,(3,2))
print(resize)

# > Flatten :Order :Transform into single dimension

print("Flatten",resize.flatten(order="F"))

# >Ravel
print("Ravel",np.ravel(resize))
print(var.data)
"""
Go and Find The Order list of Ravel and Flatten in Numpy Documentation.
---------------------------------
"""
