import numpy as np
import pandas as pd

#Basic lambda function to filter 
foo = [{
    'Language': 'Python',
    'Percent grow': 56
}, {
    'Language': 'Java',
    'Percent grow': 34
}, {
    'Language': 'C',
    'Percent grow': 25
}, {
    'Language': 'C++',
    'Percent grow': 12
}, {
    'Language': 'go',
    'Percent grow': 5
}]


df = pd.DataFrame(foo, index=pd.RangeIndex(0, len(foo)))

print(df.loc[df['Language'].isin(['Java', 'C'])])
"""
Language  Percent grow
1     Java            34
2        C            25

"""

mylambda= lambda x: x in ['C', 'C++']


print(df.loc[df['Language'].apply(mylambda)])
"""
Language  Percent grow
1     Java            34
2        C            25

"""

Numbers = {'set_of_numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(Numbers, columns=['set_of_numbers'])

df['equal_or_lower_than_4?'] = df['set_of_numbers'].apply(lambda x: 'True' if x <= 4 else 'False')

print(df)
"""
  set_of_numbers equal_or_lower_than_4?
0               1                   True
1               2                   True
2               3                   True
3               4                   True
4               5                  False
5               6                  False
6               7                  False
7               8                  False
8               9                  False
9              10                  False
"""

#Sample
"""
.sample()

The .sample() method lets you get a random set of rows of a DataFrame. 
Set the parameter n= equal to the number of rows you want. 
Sampling the dataset is one way to efficiently explore what it contains, 
and can be especially helpful when the first few rows all look similar and you want to see diverse data.

Grab a sample of the flight data to preview what kind of data you have. 
Input


data.sample(n=5)
"""    

"""
LAMBDA

def is_delayed(x):
    return x > 0

data['delayed'] = data['arr_delay'].apply(is_delayed)


OR

data['delayed'] = data['arr_delay'].apply(lambda x: x > 0)


"""


"""
APPLY

Another frequent operation is applying a function on 1D arrays to each column or row. DataFrame’s apply method does exactly this:

"""

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
"""
       b         d         e
Utah    0.235429  0.061973 -0.265048
Ohio   -1.987103  0.516082  0.660854
Texas  -0.154396  0.194660  0.097898
Oregon  0.350302  0.019020 -0.640962

"""

f =  lambda x: x.max() - x.min()
print(frame.apply(f))
"""
b    3.408025
d    3.418899
e    2.022692
dtype: float64
"""

"""
APPLYMAP



Many of the most common array statistics (like sum and mean) are DataFrame methods, so using apply is not necessary.

Element-wise Python functions can be used, too. Suppose you wanted to compute a formatted string from each floating point value in frame. 
You can do this with applymap:

"""


format =  lambda x: '%.2f' % x  
print(frame.applymap(format))  #Apply on a frame using applymap
"""
         b     d      e
Utah     0.76  0.10  -2.02
Ohio    -1.71  0.45   1.33
Texas    0.79  1.02  -0.26
Oregon   0.08  0.44  -0.86

"""

print(frame.b.apply(format))  # Apply on a individual row using apply
"""
Utah      -0.19
Ohio       0.41
Texas     -0.02
Oregon    -0.26
Name: b, dtype: object

"""


#APPLY to get sum for each column or each row

numericData = [(2, 4, 6),

               (8, 10, 12),

               (45, 50, 55)]
dataFrame = pd.DataFrame(data=numericData)
sum = dataFrame.apply(np.sum)
print("DataFrame:")
print(dataFrame)
print("Sum of each DataFrame column:")
print(sum)
print(type(sum))
print("Sum of each DataFrame row:")
sum = dataFrame.apply(np.sum, axis=1)
print(sum)
"""
DataFrame:
    0   1   2
0   2   4   6
1   8  10  12
2  45  50  55
Sum of each DataFrame column:
0    55
1    64
2    73
dtype: int64
<class 'pandas.core.series.Series'>
Sum of each DataFrame row:
0     12
1     30
2    150
dtype: int64

"""

"""
APPLY ON PANDAS DATAFRAME
This method which can be used on both on a pandas dataframe and series. The function passed as an argument typically works on rows/columns.
"""
# Dataframe generation
gfg_string = 'geeksforgeeks'
gfg_list = 5 * [pd.Series(list(gfg_string))]

gfg_df = pd.DataFrame(data=gfg_list)
print("Original dataframe:\n" + gfg_df.to_string(index=False,   header=False), end='\n\n')

# Using apply method for sorting
# rows of characters present in
# the original dataframe
new_gfg_df = gfg_df.apply(lambda x: x.sort_values(), axis=1)

print("Transformed dataframe:\n" + new_gfg_df.to_string(index=False, header=False), end='\n\n')
"""
Original dataframe:
 g  e  e  k  s  f  o  r  g  e  e  k  s
 g  e  e  k  s  f  o  r  g  e  e  k  s
 g  e  e  k  s  f  o  r  g  e  e  k  s
 g  e  e  k  s  f  o  r  g  e  e  k  s
 g  e  e  k  s  f  o  r  g  e  e  k  s

Transformed dataframe:
 e  e  e  e  f  g  g  k  k  o  r  s  s
 e  e  e  e  f  g  g  k  k  o  r  s  s
 e  e  e  e  f  g  g  k  k  o  r  s  s
 e  e  e  e  f  g  g  k  k  o  r  s  s
 e  e  e  e  f  g  g  k  k  o  r  s  s

"""

"""
APPLY ON PANDAS SERIES
"""

# Series generation
gfg_string = 'geeksforgeeks'
gfg_series = pd.Series(list(gfg_string))
print("Original series\n" + gfg_series.to_string(index=False, header=False), end='\n\n')

# Using apply method for converting characters
# present in the original series
new_gfg_series = gfg_series.apply(str.upper)
print("Transformed series:\n" +  new_gfg_series.to_string(index=False, header=False), end='\n\n')
"""
Original series
 g
 e
 e
 k
 s
 f
 o
 r
 g
 e
 e
 k
 s

Transformed series:
 G
 E
 E
 K
 S
 F
 O
 R
 G
 E
 E
 K
 S

"""


"""
APPLYMAP
This method can be used on a pandas dataframe. 
The function passed as an argument typically works on elements of the dataframe applymap() is typically used for elementwise operations
"""
# DataFrame generation
gfg_string = 'geeksforgeeks'
gfg_list = 5 * [pd.Series(list(gfg_string))]
gfg_df = pd.DataFrame(data=gfg_list)

print("Original dataframe:\n" +
      gfg_df.to_string(index=False,
                       header=False), end='\n\n')

# Using applymap method for transforming
# characters into uppercase characters
# present in the original dataframe
new_gfg_df = gfg_df.applymap(str.upper)
print("Transformed dataframe:\n" +
      new_gfg_df.to_string(index=False,
                           header=False), end='\n\n')

"""
Original dataframe:
 g  e  e  k  s  f  o  r  g  e  e  k  s
 g  e  e  k  s  f  o  r  g  e  e  k  s
 g  e  e  k  s  f  o  r  g  e  e  k  s
 g  e  e  k  s  f  o  r  g  e  e  k  s
 g  e  e  k  s  f  o  r  g  e  e  k  s

Transformed dataframe:
 G  E  E  K  S  F  O  R  G  E  E  K  S
 G  E  E  K  S  F  O  R  G  E  E  K  S
 G  E  E  K  S  F  O  R  G  E  E  K  S
 G  E  E  K  S  F  O  R  G  E  E  K  S
 G  E  E  K  S  F  O  R  G  E  E  K  S
 """



"""
 MAP ON PANDAS SERIES
 This method is used on series function, list and dictionary passed as an argument. 
 This method is generally used to map values from two series having one column same
"""

gfg_string = 'geeksforgeeks'
gfg_series = pd.Series(list(gfg_string))
print("Original series\n" +
      gfg_series.to_string(index=False,
                           header=False), end='\n\n')

# Using apply method for converting characters
# present in the original series
new_gfg_series = gfg_series.map(str.upper)
print("Transformed series:\n" +
      new_gfg_series.to_string(index=False,
                               header=False), end='\n\n')
"""
Original series
 g
 e
 e
 k
 s
 f
 o
 r
 g
 e
 e
 k
 s

Transformed series:
 G
 E
 E
 K
 S
 F
 O
 R
 G
 E
 E
 K
 S

"""