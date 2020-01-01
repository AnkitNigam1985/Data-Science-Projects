import numpy as np
import pandas as pd


a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print("\n")
"""
[[1 2]
 [3 4]
 [5 6]]
"""

print(a[[0, 1, 2], [0, 1, 0]])  # Prints elements at [0,0], [1,1], and [2,0]
print("\n")
"""
[1 4 5]

"""

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)
print("\n")
"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

"""
b = np.array([0, 2, 0, 1])
print(b)
print("\n")
"""
[0 2 0 1]
"""
print(np.arange(4))
print("\n")
"""
[0 1 2 3]
"""

print(a[np.arange(4), b])
print("\n")
# a[[0 1 2 3][0 2 0 1]]
# So, index - 00 12 20 31
"""
[ 1  6  7 11]
"""
a[np.arange(4), b] += 10
print(a[np.arange(4), b])
print("\n")

"""
[11 16 17 21]
"""


#Boolean indexing
a = np.array([[1, 2], [3, 4], [5, 6]])
boolean = (a > 3)
print(boolean)
print("\n")
"""
[[False False]
 [False  True]
 [ True  True]]
"""

print(a[boolean])
print("\n")
"""
[4 5 6]
"""


#Mathematical operations
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(np.add(a, b))  # a+b does the same
print("\n")
"""
[[ 8 10 12]
 [14 16 18]]
"""
print(np.subtract(a, b))
print("\n")
"""
[[-6 -6 -6]
 [-6 -6 -6]]
"""

#Sum
a = np.array([[1, 2], [3, 4]])
"""
1 2
3 4
"""
print(np.sum(a))  #10
print("\n")

print(np.sum(a, axis=0)) #row-wise
"""
[4 6]
"""
print(np.sum(a, axis=1)) #col-wise
"""
[ 3 7 ]
"""
print("\n")

#Transpose
print(a.T)
"""
[1 3]
[2 4]
"""
print("\n")

#Dot 
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
print(v.dot(w)) #219  (9*11 + 10*12)
print("\n")

print(x.dot(v))
print("\n") # [29 67]   1*9+2*10  3*9+4*10
print(x.dot(y))  # [19 22][43 50]   1*5 + 2*6
print("\n")