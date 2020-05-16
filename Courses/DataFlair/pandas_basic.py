import numpy as np
import pandas as pd
import datetime
import itertools


#Creating Index
dataflair_index=pd.date_range('1/1/2019', periods=8)
print(dataflair_index)

"""
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08'],
              dtype='datetime64[ns]', freq='D')

"""

#Creating Series
dataflair_s1=pd.Series(np.random.randint(100, 200, 5), index=list('abcde'))
print(dataflair_s1)
"""
a    112
b    167
c    110
d    183
e    161
dtype: int32

"""

#Creating DataFrame
dataflair_df1=pd.DataFrame(np.random.randn(8,3), index=dataflair_index, columns=['a','b','c'])
print(dataflair_df1)

"""
                   a         b         c
2019-01-01  0.587772  2.001272  0.318980
2019-01-02 -0.750293 -0.698071 -0.227790
2019-01-03 -0.141182 -1.352592 -0.536137
2019-01-04  1.374924 -2.067201 -1.809087
2019-01-05 -1.115278  0.990800  0.226233
2019-01-06 -1.081040 -0.319084 -1.174190
2019-01-07  0.285947  1.057308  2.024252
2019-01-08 -1.668864 -0.176514  0.294987

"""

#Creating Panel
#dataflair_wp1 = pd.Panel()
#dataflair_wp1=pd.Panel(np.random.randn(2,5,4), items=["Item1","Item2"], major_axis=dataflair_index, minor_axis=['A','B','C','D'])
#print(dataflair_wp1)

#Creating series
dataflair = pd.Series(np.random.randn(1000))
print("Data:")
print(dataflair)
"""
Data:
0      0.553469
1     -0.226930
2     -0.008496
3      0.848632
4      0.385246
         ...
995    0.681255
996    0.043843
997    0.050571
998    1.988968
999   -0.881560
Length: 1000, dtype: float64
"""

print("Head:")
print(dataflair.head())
"""
Head:
0    0.553469
1   -0.226930
2   -0.008496
3    0.848632
4    0.385246
dtype: float64

"""
print("Tail:")
print(dataflair.tail())
"""
Tail:
995   -0.693977
996   -0.183459
997    0.652405
998    1.302372
999   -0.386482
dtype: float64
"""

print(dataflair_df1[:2])
"""
                   a         b         c
2019-01-01  0.128232 -0.562106  0.456506
2019-01-02  0.712704  0.704092  0.931174

"""

dataflair_df1.columns = [x.upper() for x in dataflair_df1.columns]
print(dataflair_df1[:2])
"""
                   A         B         C
2019-01-01 -0.897077 -0.165515  0.135440
2019-01-02 -0.668116 -1.413738  0.286811
"""

#Create a dataframe with random series and indexes
dataflair_df = pd.DataFrame({'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                             'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                             'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
print(dataflair_df)
"""
        one       two     three
a -0.766684 -0.922963       NaN
b  1.238731 -0.821559  0.997855
c  2.134601  1.474095  0.527007
d       NaN  0.288149 -1.225754
"""

print("Row :\n", dataflair_df.iloc[1])
print("\n")
print("Column :\n", dataflair_df['two'])
"""
Row :
 one     -0.721890
two      1.194527
three   -1.564303
Name: b, dtype: float64

Column :
 a    0.564699
b    1.194527
c   -0.260891
d   -1.952266
Name: two, dtype: float64
"""

#Sub extracts the information for all the rows except one provided in sub() argument
print("=====")
print(dataflair_df.sub(dataflair_df['two'], axis='index'))
"""
=====
        one  two     three
a -2.604129  0.0       NaN
b -2.420080  0.0 -1.723317
c -0.029502  0.0 -1.625766
d       NaN  0.0 -1.018588
"""
print("=====")
print(dataflair_df.sub(dataflair_df['one'], axis='index'))
"""
=====
   one       two     three
a  0.0 -0.287199       NaN
b  0.0  2.540912  1.750263
c  0.0 -0.041552  0.424877
d  NaN       NaN       NaN
"""

#Multi-indexed DataFrame
Country=["India","England","Australia","South Africa", "New Zealand"]
Year=["1999","2003","2007","2011","2015","2019"]
heir_index = []

#Create pairs for multi index from 2 lists
for elem in itertools.product(Country,Year):
    heir_index.append(elem)

matches_won=pd.Series(np.random.randint(1,25, 30))
dfwc_index = pd.MultiIndex.from_tuples(list(heir_index), names=['Country', 'Year'])

dfwc = pd.DataFrame(data=list(matches_won),
                    index=dfwc_index, columns=['Matches Won'])
print(dfwc)
"""
                  Matches Won
Country      Year
India        1999           12
             2003            1
             2007           15
             2011           11
             2015           12
             2019           12
England      1999            4
             2003            7
             2007            4
             2011            6
             2015            4
             2019           17
Australia    1999            9
             2003           17
             2007            5
             2011           17
             2015            7
             2019           14
South Africa 1999           24
             2003            6
             2007            5
             2011           11
             2015           14
             2019           15
New Zealand  1999            5
             2003           18
             2007            4
             2011           12
             2015           12
             2019            7

"""


#Missing values in Pandas
dataflair_df2 = pd.DataFrame({'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']), 'two': pd.Series(
    np.random.randn(4), index=['a', 'b', 'c', 'd']), 'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})

print(dataflair_df2)
"""
        one       two     three
a  1.640287  0.571028       NaN
b  0.235830  0.424082 -0.160580
c  1.091303  0.042243 -0.350854
d       NaN  0.184032  0.557046
"""
dataflair_df2.fillna(0, inplace=True)
print(dataflair_df2)
"""
       one       two     three
a  1.407201 -1.436955  0.000000
b -1.235881  0.224978  0.550724
c -0.303564 -0.684714  0.568631
d  0.000000  1.506878  0.278668
"""
=======
import numpy as np
import pandas as pd
import datetime
import itertools


#Creating Index
dataflair_index=pd.date_range('1/1/2019', periods=8)
print(dataflair_index)

"""
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08'],
              dtype='datetime64[ns]', freq='D')

"""

#Creating Series
dataflair_s1=pd.Series(np.random.randint(100, 200, 5), index=list('abcde'))
print(dataflair_s1)
"""
a    112
b    167
c    110
d    183
e    161
dtype: int32

"""

#Creating DataFrame
dataflair_df1=pd.DataFrame(np.random.randn(8,3), index=dataflair_index, columns=['a','b','c'])
print(dataflair_df1)

"""
                   a         b         c
2019-01-01  0.587772  2.001272  0.318980
2019-01-02 -0.750293 -0.698071 -0.227790
2019-01-03 -0.141182 -1.352592 -0.536137
2019-01-04  1.374924 -2.067201 -1.809087
2019-01-05 -1.115278  0.990800  0.226233
2019-01-06 -1.081040 -0.319084 -1.174190
2019-01-07  0.285947  1.057308  2.024252
2019-01-08 -1.668864 -0.176514  0.294987

"""

#Creating Panel
#dataflair_wp1 = pd.Panel()
#dataflair_wp1=pd.Panel(np.random.randn(2,5,4), items=["Item1","Item2"], major_axis=dataflair_index, minor_axis=['A','B','C','D'])
#print(dataflair_wp1)

#Creating series
dataflair = pd.Series(np.random.randn(1000))
print("Data:")
print(dataflair)
"""
Data:
0      0.553469
1     -0.226930
2     -0.008496
3      0.848632
4      0.385246
         ...
995    0.681255
996    0.043843
997    0.050571
998    1.988968
999   -0.881560
Length: 1000, dtype: float64
"""

print("Head:")
print(dataflair.head())
"""
Head:
0    0.553469
1   -0.226930
2   -0.008496
3    0.848632
4    0.385246
dtype: float64

"""
print("Tail:")
print(dataflair.tail())
"""
Tail:
995   -0.693977
996   -0.183459
997    0.652405
998    1.302372
999   -0.386482
dtype: float64
"""

print(dataflair_df1[:2])
"""
                   a         b         c
2019-01-01  0.128232 -0.562106  0.456506
2019-01-02  0.712704  0.704092  0.931174

"""

dataflair_df1.columns = [x.upper() for x in dataflair_df1.columns]
print(dataflair_df1[:2])
"""
                   A         B         C
2019-01-01 -0.897077 -0.165515  0.135440
2019-01-02 -0.668116 -1.413738  0.286811
"""

#Create a dataframe with random series and indexes
dataflair_df = pd.DataFrame({'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                             'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                             'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
print(dataflair_df)
"""
        one       two     three
a -0.766684 -0.922963       NaN
b  1.238731 -0.821559  0.997855
c  2.134601  1.474095  0.527007
d       NaN  0.288149 -1.225754
"""

print("Row :\n", dataflair_df.iloc[1])
print("\n")
print("Column :\n", dataflair_df['two'])
"""
Row :
 one     -0.721890
two      1.194527
three   -1.564303
Name: b, dtype: float64

Column :
 a    0.564699
b    1.194527
c   -0.260891
d   -1.952266
Name: two, dtype: float64
"""

#Sub extracts the information for all the rows except one provided in sub() argument
print("=====")
print(dataflair_df.sub(dataflair_df['two'], axis='index'))
"""
=====
        one  two     three
a -2.604129  0.0       NaN
b -2.420080  0.0 -1.723317
c -0.029502  0.0 -1.625766
d       NaN  0.0 -1.018588
"""
print("=====")
print(dataflair_df.sub(dataflair_df['one'], axis='index'))
"""
=====
   one       two     three
a  0.0 -0.287199       NaN
b  0.0  2.540912  1.750263
c  0.0 -0.041552  0.424877
d  NaN       NaN       NaN
"""

#Multi-indexed DataFrame
Country=["India","England","Australia","South Africa", "New Zealand"]
Year=["1999","2003","2007","2011","2015","2019"]
heir_index = []

#Create pairs for multi index from 2 lists
for elem in itertools.product(Country,Year):
    heir_index.append(elem)

matches_won=pd.Series(np.random.randint(1,25, 30))
dfwc_index = pd.MultiIndex.from_tuples(list(heir_index), names=['Country', 'Year'])

dfwc = pd.DataFrame(data=list(matches_won),
                    index=dfwc_index, columns=['Matches Won'])
print(dfwc)
"""
                  Matches Won
Country      Year
India        1999           12
             2003            1
             2007           15
             2011           11
             2015           12
             2019           12
England      1999            4
             2003            7
             2007            4
             2011            6
             2015            4
             2019           17
Australia    1999            9
             2003           17
             2007            5
             2011           17
             2015            7
             2019           14
South Africa 1999           24
             2003            6
             2007            5
             2011           11
             2015           14
             2019           15
New Zealand  1999            5
             2003           18
             2007            4
             2011           12
             2015           12
             2019            7

"""


#Missing values in Pandas
dataflair_df2 = pd.DataFrame({'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']), 'two': pd.Series(
    np.random.randn(4), index=['a', 'b', 'c', 'd']), 'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})

print(dataflair_df2)
"""
        one       two     three
a  1.640287  0.571028       NaN
b  0.235830  0.424082 -0.160580
c  1.091303  0.042243 -0.350854
d       NaN  0.184032  0.557046
"""
dataflair_df2.fillna(0, inplace=True)
print(dataflair_df2)
"""
       one       two     three
a  1.407201 -1.436955  0.000000
b -1.235881  0.224978  0.550724
c -0.303564 -0.684714  0.568631
d  0.000000  1.506878  0.278668
"""
