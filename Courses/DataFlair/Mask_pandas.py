import numpy as np
import pandas as pd

"""
DataFrame.mask(self, cond, other=nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False)
Replace values where the condition is True.

The mask method is an application of the if-then idiom. For each element in the calling DataFrame, if cond is False the element is used; otherwise the corresponding element from the DataFrame other is used.

The signature for DataFrame.where() differs from numpy.where(). Roughly df1.where(m, df2) is equivalent to np.where(m, df1, df2).

"""

s = pd.Series(range(5))
print(s)
"""
0    0
1    1
2    2
3    3
4    4
dtype: int64
"""

print(s.where(s>1))  #set defult value NaN where condition is False
"""
0    NaN
1    NaN
2    2.0
3    3.0
4    4.0
dtype: float64
"""

print(s.mask(s>1))  #set default value NaN where condition is True
"""
0    0.0
1    1.0
2    NaN
3    NaN
4    NaN
dtype: float64
"""

print(s.where(s > 1, 10)) #set given value 10 where condition is False
"""
0    10
1    10
2     2
3     3
4     4
dtype: int64
"""

print(s.mask(s > 1, 10))  # set given value 10 where condition is True
"""
0     0
1     1
2    10
3    10
4    10
dtype: int64
"""

df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])

print(df)
"""
A  B
0  0  1
1  2  3
2  4  5
3  6  7
4  8  9

"""

m=df%3==0

print(df.where(m, -df))  #Set the value to -ve where condition is False
"""
A  B
0  0 -1
1 -2  3
2 -4 -5
3  6 -7
4 -8  9

"""

print(df.mask(m, -df)) #Set the value to -ve where condition is True
"""
 A  B
0  0  1
1  2 -3
2  4  5
3 -6  7
4  8 -9

=======
import numpy as np
import pandas as pd

"""
DataFrame.mask(self, cond, other=nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False)
Replace values where the condition is True.

The mask method is an application of the if-then idiom. For each element in the calling DataFrame, if cond is False the element is used; otherwise the corresponding element from the DataFrame other is used.

The signature for DataFrame.where() differs from numpy.where(). Roughly df1.where(m, df2) is equivalent to np.where(m, df1, df2).

"""

s = pd.Series(range(5))
print(s)
"""
0    0
1    1
2    2
3    3
4    4
dtype: int64
"""

print(s.where(s>1))  #set defult value NaN where condition is False
"""
0    NaN
1    NaN
2    2.0
3    3.0
4    4.0
dtype: float64
"""

print(s.mask(s>1))  #set default value NaN where condition is True
"""
0    0.0
1    1.0
2    NaN
3    NaN
4    NaN
dtype: float64
"""

print(s.where(s > 1, 10)) #set given value 10 where condition is False
"""
0    10
1    10
2     2
3     3
4     4
dtype: int64
"""

print(s.mask(s > 1, 10))  # set given value 10 where condition is True
"""
0     0
1     1
2    10
3    10
4    10
dtype: int64
"""

df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])

print(df)
"""
A  B
0  0  1
1  2  3
2  4  5
3  6  7
4  8  9

"""

m=df%3==0

print(df.where(m, -df))  #Set the value to -ve where condition is False
"""
A  B
0  0 -1
1 -2  3
2 -4 -5
3  6 -7
4 -8  9

"""

print(df.mask(m, -df)) #Set the value to -ve where condition is True
"""
 A  B
0  0  1
1  2 -3
2  4  5
3 -6  7
4  8 -9

"""