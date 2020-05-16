import numpy as np
import pandas as pd


#Pipe() used to apply any operation on all elements of series or dataframe

#Creating a function to be applied using pipe()
def adder(ele1, ele2):
    return ele1+ele2

#Series
print("\nSeries:\n")
dataflair_s1 = pd.Series([11, 21, 31, 41, 51])
print("Original :\n",dataflair_s1)

print("After pipe():\n", dataflair_s1.pipe(adder, 3))
"""
Original :
 0    11
1    21
2    31
3    41
4    51
dtype: int64
After pipe():
 0    14
1    24
2    34
3    44
4    54
dtype: int64
"""


#DataFrame
dataflair_df1 = pd.DataFrame(
    6*np.random.randn(6, 3), columns=['c1', 'c2', 'c3'])
print("Original Dataframe :\n", dataflair_df1)

print("After pipe():\n", dataflair_df1.pipe(adder, 3))
"""
Original Dataframe :
           c1         c2         c3
0   7.846747  -2.022487  -4.943301
1  -0.857617  -3.749087   7.165374
2  12.145709  11.951062   4.020946
3   1.778519   5.065232 -12.122106
4  -4.958476  -7.021716  -4.242996
5   0.358903  -3.543973   4.067560
After pipe():
           c1         c2         c3
0  10.846747   0.977513  -1.943301
1   2.142383  -0.749087  10.165374
2  15.145709  14.951062   7.020946
3   4.778519   8.065232  -9.122106
4  -1.958476  -4.021716  -1.242996
"""

=======
import numpy as np
import pandas as pd


#Pipe() used to apply any operation on all elements of series or dataframe

#Creating a function to be applied using pipe()
def adder(ele1, ele2):
    return ele1+ele2

#Series
print("\nSeries:\n")
dataflair_s1 = pd.Series([11, 21, 31, 41, 51])
print("Original :\n",dataflair_s1)

print("After pipe():\n", dataflair_s1.pipe(adder, 3))
"""
Original :
 0    11
1    21
2    31
3    41
4    51
dtype: int64
After pipe():
 0    14
1    24
2    34
3    44
4    54
dtype: int64
"""


#DataFrame
dataflair_df1 = pd.DataFrame(
    6*np.random.randn(6, 3), columns=['c1', 'c2', 'c3'])
print("Original Dataframe :\n", dataflair_df1)

print("After pipe():\n", dataflair_df1.pipe(adder, 3))
"""
Original Dataframe :
           c1         c2         c3
0   7.846747  -2.022487  -4.943301
1  -0.857617  -3.749087   7.165374
2  12.145709  11.951062   4.020946
3   1.778519   5.065232 -12.122106
4  -4.958476  -7.021716  -4.242996
5   0.358903  -3.543973   4.067560
After pipe():
           c1         c2         c3
0  10.846747   0.977513  -1.943301
1   2.142383  -0.749087  10.165374
2  15.145709  14.951062   7.020946
3   4.778519   8.065232  -9.122106
4  -1.958476  -4.021716  -1.242996
"""

