import numpy as np
import pandas as pd

dataflair_arr = pd.Series([2, 3, -4, 6])
print(dataflair_arr)
"""
0    2
1    3
2   -4
3    6
dtype: int64
"""

npa = np.array(['d', 'a', 't', 'a'])
dataflair_ar = pd.Series(npa)
print(dataflair_ar)
"""
0    d
1    a
2    t
3    a
dtype: object
"""

dataflair_dict = {'Delhi': 12.9, 'Mumbai': 8.4, 'Kolkata': 9.7}
dataflair_arr3 = pd.Series(dataflair_dict)
print(dataflair_arr3)
"""
Delhi      12.9
Mumbai      8.4
Kolkata     9.7
dtype: float64
"""
df = dataflair_arr3.reset_index() #reset index will convert series to dataframe
df.columns=['City','Distance']
print(df)
print(type(df))
"""
    City  Distance
0    Delhi      12.9
1   Mumbai       8.4
2  Kolkata       9.7
<class 'pandas.core.frame.DataFrame'>
"""
#Changing index of Series
num=['n1','n2','n3','n4']
dataflair_arr2 = pd.Series([4, 5, -2, 2], index=num)
print(dataflair_arr2)
"""
n1    4
n2    5
n3   -2
n4    2
dtype: int64
"""

print(dataflair_arr2[dataflair_arr2 > 2])
"""
n1    4
n2    5
dtype: int64
"""

print(dataflair_arr2*5)
"""
dtype: int64
n1    20
n2    25
n3   -10
n4    10
dtype: int64

"""


#Missing values

dataflair_arr4 = pd.Series(dataflair_dict)
print(dataflair_arr4)
"""
Delhi      12.9
Mumbai      8.4
Kolkata     9.7
"""
cities = ['Delhi', 'Kolkata', 'Mumbai', 'Chennai']
dataflair_arr4 = pd.Series(dataflair_dict, index=cities)
print(dataflair_arr4)
"""
Delhi      12.9
Kolkata     9.7
Mumbai      8.4
Chennai     NaN
dtype: float64
"""

#Addition of 2 series
print(dataflair_arr4+dataflair_arr3)
"""
Chennai     NaN
Delhi      25.8
Kolkata    19.4
Mumbai     16.8
dtype: float64
"""

#Accessing the elements using  range
print(dataflair_arr4[:2])
"""
Delhi      12.9
Kolkata     9.7
dtype: float64
"""


=======
import numpy as np
import pandas as pd

dataflair_arr = pd.Series([2, 3, -4, 6])
print(dataflair_arr)
"""
0    2
1    3
2   -4
3    6
dtype: int64
"""

npa = np.array(['d', 'a', 't', 'a'])
dataflair_ar = pd.Series(npa)
print(dataflair_ar)
"""
0    d
1    a
2    t
3    a
dtype: object
"""

dataflair_dict = {'Delhi': 12.9, 'Mumbai': 8.4, 'Kolkata': 9.7}
dataflair_arr3 = pd.Series(dataflair_dict)
print(dataflair_arr3)
"""
Delhi      12.9
Mumbai      8.4
Kolkata     9.7
dtype: float64
"""
df = dataflair_arr3.reset_index() #reset index will convert series to dataframe
df.columns=['City','Distance']
print(df)
print(type(df))
"""
    City  Distance
0    Delhi      12.9
1   Mumbai       8.4
2  Kolkata       9.7
<class 'pandas.core.frame.DataFrame'>
"""
#Changing index of Series
num=['n1','n2','n3','n4']
dataflair_arr2 = pd.Series([4, 5, -2, 2], index=num)
print(dataflair_arr2)
"""
n1    4
n2    5
n3   -2
n4    2
dtype: int64
"""

print(dataflair_arr2[dataflair_arr2 > 2])
"""
n1    4
n2    5
dtype: int64
"""

print(dataflair_arr2*5)
"""
dtype: int64
n1    20
n2    25
n3   -10
n4    10
dtype: int64

"""


#Missing values

dataflair_arr4 = pd.Series(dataflair_dict)
print(dataflair_arr4)
"""
Delhi      12.9
Mumbai      8.4
Kolkata     9.7
"""
cities = ['Delhi', 'Kolkata', 'Mumbai', 'Chennai']
dataflair_arr4 = pd.Series(dataflair_dict, index=cities)
print(dataflair_arr4)
"""
Delhi      12.9
Kolkata     9.7
Mumbai      8.4
Chennai     NaN
dtype: float64
"""

#Addition of 2 series
print(dataflair_arr4+dataflair_arr3)
"""
Chennai     NaN
Delhi      25.8
Kolkata    19.4
Mumbai     16.8
dtype: float64
"""

#Accessing the elements using  range
print(dataflair_arr4[:2])
"""
Delhi      12.9
Kolkata     9.7
dtype: float64
"""


