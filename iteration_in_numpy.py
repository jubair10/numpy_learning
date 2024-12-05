"""    Iteration    """
import numpy as np

var = np.array([9, 8, 7, 6])
for i in var:
    print(i) # 9 8 7 6

var1 = np.array([[9, 8, 7], [4, 5, 6]])
for i in var1:
    print(i)
# Output:
# [9 8 7]
# [4 5 6]

for i in var1:                              
    for j in i:
        print(j)
# Output:
# 9
# 8
# 7
# 4
# 5
# 6
var2 = np.array([[[1,2,3,4],[1,2,3,4]]])

for i in var2:
    for j in i:
        for k in j:
            print(k)


"""     Smartest Way    """
#                          to store value |  value type   ["S"]
for i in np.nditer(var2,flags=['buffered'],op_dtypes=[np.string_]):
    print(np.nditer(var2,flags=['buffered'],op_dtypes=[np.string_]))
    print(i)
# same as line 19 to 24

print("ndenumerate")
print(var2)
for i,d in np.ndenumerate(var2):
    print((i,d))
"""
Output:
 Index      Value
((0, 0, 0), 1)
((0, 0, 1), 2)
((0, 0, 2), 3)
((0, 0, 3), 4)
((0, 1, 0), 1)
((0, 1, 1), 2)
((0, 1, 2), 3)
((0, 1, 3), 4)
"""