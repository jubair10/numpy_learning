#
## Arithmetic Operation
#
import numpy as np

# var = np.array([1, 2, 3, 4])
# var1 = np.array([1, 2, 3, 4])

# sum = var % 3

# print(sum)

"""
2D Array
"""

# var = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
# var1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])

# print(var)
# print()
# print(var1)
# print()
# sum = np.reciprocal(var,dtype=np.float16)

# print(sum)

"""
-----------------------------
I have do this.
-----------------------------
"""

# l = [1, 2, 3]
# x = np.array((l,l,l),ndmin=2)
# print(x)

# y = np.ones((3, 3))
# print(x)
# print()
# z = np.eye(3,dtype=np.int32)
# print(z,"\n")
# print(np.reciprocal(z,x))


"""
2nd Part
--------------------------------------------------------
"""

var = np.array([1, 2, 3, 4, 5, 3, 2])


print(np.min(var))  # 1
print(np.max(var))  # 5

print(
    "Min : Value: ", np.min(var), " , Index: ", np.argmin(var)
)  # Min : Value:  1  , Index:  0
print(
    "Max : Value: ", np.max(var), " , Index: ", np.argmax(var)
)  # Max : Value:  5  , Index:  4

## *********
"""
AXIS   ATTITUDE
0       COLUMN
1       ROW
"""
var1 = np.array([[2, 3, 1], [9, 5, 6]])
#                             value index
print(np.min(var1, axis=1))  # [ 1       5]
#                               no inddex
print(np.min(var1, axis=0), "\n")  # [2 3 1]

# floating value
print(
    np.sqrt(var), "\n"
)  # [1. 1.41421356  1.73205081 2.  2.23606798 1.73205081  1.41421356]


########## Give Sin value of the Array
var2 = np.array([1, 2, 3])
dim2_var2 = np.array([[1, 2, 3], [1, 2, 3]])
print(np.sin(var2))  # [0.84147098 0.90929743 0.14112001]
print(np.sin(dim2_var2)) #
"""
[[0.84147098 0.90929743 0.14112001]
 [0.84147098 0.90929743 0.14112001]]
"""
# same goes for COS
print(np.cos(var2)) #[ 0.54030231 -0.41614684 -0.9899925 ]

"""
[1,   2,   3]

[1,   3,   6]

ক্রমযোজিত গ্ণসংখ্যার মতো |
"""

