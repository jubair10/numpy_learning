"""
Copy vs View
"""
"""
Differrence:
-----------------------------------
Copy:
1. The copy owns the data.
2. The copy of an array is a new array.
3. The changes made in the copy data doesn't reflect in the original one.

View:
1. The view doesn't own the data.
2. A view of the original array.
3. Any changes made to the view will affect the original array.
4. And, any changes made to the original array will afffect the view.
"""
import numpy as np

# Copy
var = np.array([1, 2, 3, 4])
print("var: ", var)
co = var.copy()
print("copy: ", co)
co[0] = 10
print(co)  # [10  2  3  4]
print(var)  # [1  2  3  4]
# View
vi = var.view()
print("view: ", vi)
vi[0] = 10
print(vi)  # [10  2  3  4]
print(var)  # [10  2  3  4]
