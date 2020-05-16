import numpy as np
import pandas as pd


dataflair_a= pd.Series([1,2,3,4])
print(dataflair_a)
print("\n")
"""
0    1
1    2
2    3
3    4
dtype: int64
"""

dataflair_b = pd.Series([5, 6, 7, 8])
print(dataflair_b)
print("\n")
"""
0    5
1    6
2    7
3    8
dtype: int64
"""

print(pd.concat([dataflair_a, dataflair_b]))
print("\n")
"""
0    1
1    2
2    3
3    4
0    5
1    6
2    7
3    8
dtype: int64
"""
print(pd.concat([dataflair_a, dataflair_b], ignore_index=True))
print("\n")
"""
0    1
1    2
2    3
3    4
4    5
5    6
6    7
7    8
dtype: int64
"""


#Heirarchical index on pandas series
print(pd.concat([dataflair_a, dataflair_b], keys=['a', 'b', ]))
print("\n")
"""
a  0    1
   1    2
   2    3
   3    4
b  0    5
   1    6
   2    7
   3    8
dtype: int64
"""

#label the index
print(pd.concat([dataflair_a, dataflair_b], keys=[
          'a', 'b'], names=['Series name', 'Row ID']))
print("\n")
"""
Series name  Row ID
a            0         1
             1         2
             2         3
             3         4
b            0         5
             1         6
             2         7
             3         8
dtype: int64
"""

#Concatenate data frames
dataflair_A = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
dataflair_B = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])

print(dataflair_A)
print("\n")
"""
    letter  number
0      a       1
1      b       2
"""

print(dataflair_B)
print("\n")
"""
    letter  number
0      c       3
1      d       4
"""

#Using concatenate
print(pd.concat([dataflair_A,dataflair_B]))
print("\n")
"""
    letter  number
0      a       1
1      b       2
0      c       3
1      d       4
"""


#Using concate with inner join -only common columns considered
print(pd.concat([dataflair_A, dataflair_B], join="inner"))
print("\n")
"""
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
"""

#Concat horizontally
print(pd.concat([dataflair_A, dataflair_B], axis=1))
print("\n")
"""
  letter  number letter  number
0      a       1      c       3
1      b       2      d       4
"""

#Using append
dataflair_A=pd.DataFrame(
    [['a', 1], ['b', 2]], columns=['letter', 'number'])
print("Original dataflair_A :\n", dataflair_A)
print("\n") 
"""
Original dataflair_A :
   letter  number
0      a       1
1      b       2
"""

dataflair_B = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
print("Original dataflair_B :\n", dataflair_B)
"""
Original dataflair_B :
   letter  number
0      c       3
1      d       4
"""

print(dataflair_A.append(dataflair_B))
print("\n")
"""
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
"""

#Ignoring index while concatenation
print(pd.concat([dataflair_A, dataflair_B], ignore_index=True))
print("\n")
"""
  letter  number
0      a       1
1      b       2
2      c       3
3      d       4
"""
=======
import numpy as np
import pandas as pd


dataflair_a= pd.Series([1,2,3,4])
print(dataflair_a)
print("\n")
"""
0    1
1    2
2    3
3    4
dtype: int64
"""

dataflair_b = pd.Series([5, 6, 7, 8])
print(dataflair_b)
print("\n")
"""
0    5
1    6
2    7
3    8
dtype: int64
"""

print(pd.concat([dataflair_a, dataflair_b]))
print("\n")
"""
0    1
1    2
2    3
3    4
0    5
1    6
2    7
3    8
dtype: int64
"""
print(pd.concat([dataflair_a, dataflair_b], ignore_index=True))
print("\n")
"""
0    1
1    2
2    3
3    4
4    5
5    6
6    7
7    8
dtype: int64
"""


#Heirarchical index on pandas series
print(pd.concat([dataflair_a, dataflair_b], keys=['a', 'b', ]))
print("\n")
"""
a  0    1
   1    2
   2    3
   3    4
b  0    5
   1    6
   2    7
   3    8
dtype: int64
"""

#label the index
print(pd.concat([dataflair_a, dataflair_b], keys=[
          'a', 'b'], names=['Series name', 'Row ID']))
print("\n")
"""
Series name  Row ID
a            0         1
             1         2
             2         3
             3         4
b            0         5
             1         6
             2         7
             3         8
dtype: int64
"""

#Concatenate data frames
dataflair_A = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
dataflair_B = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])

print(dataflair_A)
print("\n")
"""
    letter  number
0      a       1
1      b       2
"""

print(dataflair_B)
print("\n")
"""
    letter  number
0      c       3
1      d       4
"""

#Using concatenate
print(pd.concat([dataflair_A,dataflair_B]))
print("\n")
"""
    letter  number
0      a       1
1      b       2
0      c       3
1      d       4
"""


#Using concate with inner join -only common columns considered
print(pd.concat([dataflair_A, dataflair_B], join="inner"))
print("\n")
"""
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
"""

#Concat horizontally
print(pd.concat([dataflair_A, dataflair_B], axis=1))
print("\n")
"""
  letter  number letter  number
0      a       1      c       3
1      b       2      d       4
"""

#Using append
dataflair_A=pd.DataFrame(
    [['a', 1], ['b', 2]], columns=['letter', 'number'])
print("Original dataflair_A :\n", dataflair_A)
print("\n") 
"""
Original dataflair_A :
   letter  number
0      a       1
1      b       2
"""

dataflair_B = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
print("Original dataflair_B :\n", dataflair_B)
"""
Original dataflair_B :
   letter  number
0      c       3
1      d       4
"""

print(dataflair_A.append(dataflair_B))
print("\n")
"""
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
"""

#Ignoring index while concatenation
print(pd.concat([dataflair_A, dataflair_B], ignore_index=True))
print("\n")
"""
  letter  number
0      a       1
1      b       2
2      c       3
3      d       4
"""
