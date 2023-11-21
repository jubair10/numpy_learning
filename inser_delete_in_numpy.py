"""    Insert and Delete"""
import numpy as np

"""    Insert   """
var = np.array([1, 2, 3, 4])
print(var)
print(var.dtype)
print(type(var))

ins = np.insert(
    var,  (2,1) ,44
)
print(ins) # [ 1  2 44  3  4]

var_2dim = np.array([[1,2,3],[1,2,3]])
print(var_2dim)

# ins1=np.insert(var_2dim, 2 ,6,axis=0)
"""
[[1 2 3]
 [1 2 3]
 [6 6 6]]"""
# ins1=np.insert(var_2dim, 2 ,6,axis=1)
"""
[[1 2 6 3]
 [1 2 6 3]]
"""
#------------ for multiple value use a list
# ins1=np.insert(var_2dim, 2 ,[6,25],axis=1)
# print(ins1)

# Append like python's list append function
x = np.append(var,6.5)
print(x)

# x2 = np.append(var_2dim,[[45,56,78]],axis=0)
"""
[[ 1  2  3]
 [ 1  2  3]
 [45 56 78]]"""
# print(x2)


"""    Delete   """

delt = np.delete(var,2) # [1 2 4]
print(delt)