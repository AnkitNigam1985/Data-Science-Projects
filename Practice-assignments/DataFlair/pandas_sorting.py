import numpy as np
import pandas as pd

#1-D array
dataflair_ar1=np.array([4,6,7,5])
print(dataflair_ar1)
print("\n")
"""
[4 6 7 5]
"""

#2-D array
dataflair_ar2=np.array ([[4,6,5],[9,8,7]])
print(dataflair_ar2)
print("\n")
"""
[[4 6 5]
 [9 8 7]]

"""

dataflair_ar1.sort()
dataflair_ar2.sort()

print(dataflair_ar1)
print("\n")
"""
[4 5 6 7]
"""

print(dataflair_ar2)
print("\n")
"""
[[4 5 6]
 [7 8 9]]

"""

#Sort the 2-D array along x-axis
dataflair_ar4=np.array([[9,8],[11,0]])
print(dataflair_ar4)
print("\n")
"""
[[ 9  8]
 [11  0]]
"""

dataflair_ar4.sort(axis=0)
print(dataflair_ar4)
print("\n")
"""
[[ 9  0]
 [11  8]]
"""

#Sort the 2-D array along y-axis - along the column
dataflair_ar4 = np.array([[9, 8], [11, 0]])
print(dataflair_ar4)
print("\n")
"""
[[ 9  8]
 [11  0]]
"""

dataflair_ar4.sort(axis=1) #along the row
print(dataflair_ar4)
print("\n")
"""
[[ 8  9]
 [ 0 11]]
"""

#Sorting the pandas dataframe
dataflair_se = pd.Series([np.nan, 3, 7, 11, 8])
print(dataflair_se)
print("\n")
"""
0     NaN
1     3.0
2     7.0
3    11.0
4     8.0
dtype: float64
"""

print(dataflair_se.sort_values(ascending=True))
print("\n")

"""
1     3.0
2     7.0
4     8.0
3    11.0
0     NaN
dtype: float64

"""

#Sorting values while putting NaN first
print(dataflair_se.sort_values(na_position='first'))
print("\n")
"""
0     NaN
1     3.0
2     7.0
4     8.0
3    11.0
dtype: float64
"""


dataflair_df1 = pd.DataFrame({'col1': [5, 2, 5, 2, 2, 1], 'col2': [
                             'C', 'B', 'A', np.nan, 'C', 'D'], 'col3': [9, 6, 0, 7, 5, 8]})
print(dataflair_df1)
print("\n")

"""
    col1 col2  col3
0     5    C     9
1     2    B     6
2     5    A     0
3     2  NaN     7
4     2    C     5
5     1    D     8
"""

print("Sort by a single column:\n")
print(dataflair_df1.sort_values(by=['col1']))
print("\n")
"""
Sort by a single column:

   col1 col2  col3
5     1    D     8
1     2    B     6
3     2  NaN     7
4     2    C     5
0     5    C     9
2     5    A     0
"""

print("Sort by multiple columns :\n")
print(dataflair_df1.sort_values(by=['col1', 'col2']))
print("\n")
"""
Sort by multiple columns :

   col1 col2  col3
5     1    D     8
1     2    B     6
4     2    C     5
3     2  NaN     7
2     5    A     0
0     5    C     9
"""

#Sorting using dataframe IndexError
dataflair_df1 = pd.DataFrame({'col3' : [9, 6, 0, 7, 5, 8],'col1' : ['C', 'B', 'A', np.nan, 'C', 'D'],'col2': [20, 3, 5, 18, 15, 1],})
print("Original dataframe :\n", dataflair_df1)

print(dataflair_df1.sort_index(axis = 1))
print("\n")
"""
  col1  col2  col3
0    C    20     9
1    B     3     6
2    A     5     0
3  NaN    18     7
4    C    15     5
5    D     1     8
"""

print(dataflair_df1.sort_index(axis = 0))
print("\n")
"""
   col3 col1  col2
0     9    C    20
1     6    B     3
2     0    A     5
3     7  NaN    18
4     5    C    15
5     8    D     1
"""

print(dataflair_df1.reindex(sorted(dataflair_df1.columns), axis=1))
"""
col1  col2  col3
0    C    20     9
1    B     3     6
2    A     5     0
3  NaN    18     7
4    C    15     5
5    D     1     8
"""

#Sort dataframe using Index
dataflair_df1 = pd.DataFrame({'col3' : [4,8,7,9,3,5],'col1' : [14,18,27,29,6,1],'col2': [3,6,9,2,4,8]},index=['A','B','C','D','E','F'])
print("\nOriginal Dataframe :\n", dataflair_df1)
print("\n")
print(dataflair_df1.sort_values(by='D', axis=1))
#Value in row D is sorted and corresponding columns arranged for remaining dataframe
"""
col2  col3  col1
A     3     4    14
B     6     8    18
C     9     7    27
D     2     9    29
E     4     3     6
F     8     5     1
"""
print("\n")
#print(dataflair_df1.sort_values(by='D', axis=0)) Error