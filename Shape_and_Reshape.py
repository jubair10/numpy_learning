"""
Shape and Reshape
"""
import numpy as np

var  = np.array([[1,2,3,4],[1,2,3,4]])
print(var,"\n")
print(np.shape(var)) # (2, 4)

var1=np.array([1,2,3,4],ndmin=4)
print(np.shape(var1)) # (1, 1, 1, 4)

## Reshape: to Change Dimension 
"""
----Very important ----
Reshape Must be equal to the size -----------
of the array to be shaped--------------------
"""
var2 = np.array([1,2,3,4,5,6])
x = var2.reshape(3,2,1)
print(x)
#
print(x.reshape(-1)) # [1 2 3 4 5 6] ---
# It converts any array to One Dimension