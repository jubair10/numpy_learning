"""
Broadcasting 

broadcasting is nothing but doing operations like add , subtraction ETC.
Condition:
1.Same Dimension
2.Compare
"""
import numpy as np

# to Broadcasrt Dimension must be same.
# then we should  compare first
# SHAPE doesn't matter but Dimesion does--- That mean (3, 1) and (1, 3) can be broadcasted
var = np.array([1, 2, 3])
var1 = np.array([1, 2, 3])

# print(var+var1)  -- Broadcasting Error
print(var + var1, "\n")
var2 = np.array([[1], [2], [3]])
var3 = np.array([[1,1,1], [2,2,2,], [3,3,3]])

print(var2)

print(var2 + var3)
"""
Output:
-----------
[[2 2 2]
 [4 4 4]
 [6 6 6]]
"""
print(var + var2)
"""
Output:
-----------
[[2 3 4]
 [3 4 5]
 [4 5 6]]
"""
