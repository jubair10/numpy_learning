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
var =np.array([1,2,3,4])
var1=np.array([1,2,3,])

# print(var+var1)  -- Broadcasting Error
print(var+var1)