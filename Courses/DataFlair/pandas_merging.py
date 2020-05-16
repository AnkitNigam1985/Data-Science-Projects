import numpy as np
import pandas as pd

dataflair = {
    'item no.': [1, 2, 3, 4, 5],
    'category': ['vegetable', 'vegetable', 'fruit', 'vegetable', 'fruit'],
    'name': ['carrot', 'beans', 'apple', 'potato', 'grapes']
}

a = pd.DataFrame(dataflair, columns=['item no.', 'category', 'name'])
print("DataFrame :\n", a)
"""
DataFrame :
    item no.   category    name
0         1  vegetable  carrot
1         2  vegetable   beans
2         3      fruit   apple
3         4  vegetable  potato
4         5      fruit  grapes

"""

dataflair2 = {
    'item no.': [4, 5, 6, 7, 8],
    'category': ['vegetable', 'fruit', 'fruit', 'vegetable', 'fruit'],
    'name': ['gourd', 'mango', 'peach', 'peas', 'watermelon']
}

b = pd.DataFrame(dataflair2, columns=['item no.', 'category', 'name'])
print("DataFrame :\n", b)
"""
DataFrame :
    item no.   category        name
0         4  vegetable       gourd
1         5      fruit       mango
2         6      fruit       peach
3         7  vegetable        peas
4         8      fruit  watermelon
"""

dataflair3 = {
       'item no.':[1,2,3,4,5,6,7,8,9,10],
        'price':[12,23,98,15,88,24,67,58,26,96]
}

c = pd.DataFrame(dataflair3, columns=['item no.', 'price'])
print("DataFrame :\n", c)
"""
DataFrame :
    item no.  price
0         1     12
1         2     23
2         3     98
3         4     15
4         5     88
5         6     24
6         7     67
7         8     58
8         9     26
9        10     96
"""

#PANDAS CONCATENATION

new_vdataflair=pd.concat([a,b])
print(new_vdataflair)
print("\n")
"""
   item no.   category        name
0         1  vegetable      carrot
1         2  vegetable       beans
2         3      fruit       apple
3         4  vegetable      potato
4         5      fruit      grapes
0         4  vegetable       gourd
1         5      fruit       mango
2         6      fruit       peach
3         7  vegetable        peas
4         8      fruit  watermelon
"""

#This gives us a DataFrame, with a and b together. 
# But this is vertical; to add horizontally, we use the following function:

new_hdataflair = pd.concat([a, b], axis=1)
print(new_hdataflair)
print("\n")
"""
   item no.   category    name  item no.   category        name
0         1  vegetable  carrot         4  vegetable       gourd
1         2  vegetable   beans         5      fruit       mango
2         3      fruit   apple         6      fruit       peach
3         4  vegetable  potato         7  vegetable        peas
4         5      fruit  grapes         8      fruit  watermelon
"""

#PANDAS MERGE
dataflair_x=pd.merge(new_vdataflair, c, on='item no.')
print(dataflair_x)
print("\n")
"""
   item no.   category        name  price
0         1  vegetable      carrot     12
1         2  vegetable       beans     23
2         3      fruit       apple     98
3         4  vegetable      potato     15
4         4  vegetable       gourd     15
5         5      fruit      grapes     88
6         5      fruit       mango     88
7         6      fruit       peach     24
8         7  vegetable        peas     67
9         8      fruit  watermelon     58
"""

#Pandas merging on multiple columns
dataflair_mkeys = pd.merge(a, b, on=['item no.', 'category'])
print(dataflair_mkeys)
print("\n")
"""
   item no.   category  name_x name_y
0         4  vegetable  potato  gourd
1         5      fruit  grapes  mango
"""

#Pandas merging on basis of index
"""
DataFrame :
    item no.   category    name
0         1  vegetable  carrot
1         2  vegetable   beans
2         3      fruit   apple
3         4  vegetable  potato
4         5      fruit  grapes
DataFrame :
    item no.   category        name
0         4  vegetable       gourd
1         5      fruit       mango
2         6      fruit       peach
3         7  vegetable        peas
4         8      fruit  watermelon
"""
new6_dataflair = pd.merge(a, b, right_index=True, left_index=True)
print(new6_dataflair)
print("\n")
"""
  item no._x category_x  name_x  item no._y category_y      name_y
0           1  vegetable  carrot           4  vegetable       gourd
1           2  vegetable   beans           5      fruit       mango
2           3      fruit   apple           6      fruit       peach
3           4  vegetable  potato           7  vegetable        peas
4           5      fruit  grapes           8      fruit  watermelon

"""


#PANDAS OUTER JOIN
new2_dataflair = pd.merge(a, b, on='item no.', how='outer')
print(new2_dataflair)
print("\n")
"""
   item no. category_x  name_x category_y      name_y
0         1  vegetable  carrot        NaN         NaN
1         2  vegetable   beans        NaN         NaN
2         3      fruit   apple        NaN         NaN
3         4  vegetable  potato  vegetable       gourd
4         5      fruit  grapes      fruit       mango
5         6        NaN     NaN      fruit       peach
6         7        NaN     NaN  vegetable        peas
7         8        NaN     NaN      fruit  watermelon
"""

#PANDAS INNER JOIN
new3_dataflair = pd.merge(a, b, on='item no.', how='inner')
print(new3_dataflair)
print("\n")
"""
  item no. category_x  name_x category_y name_y
0         4  vegetable  potato  vegetable  gourd
1         5      fruit  grapes      fruit  mango
"""
new3_xdataflair = pd.merge(a, b, on='item no.', how='inner', right_index=True, left_index=True)
print(new3_xdataflair)
print("\n")
"""
   item no. category_x  name_x category_y      name_y
0         1  vegetable  carrot  vegetable       gourd
1         2  vegetable   beans      fruit       mango
2         3      fruit   apple      fruit       peach
3         4  vegetable  potato  vegetable        peas
4         5      fruit  grapes      fruit  watermelon
"""
new3_xdataflair = pd.merge(
    a, b,  right_index=True, left_index=True)
print(new3_xdataflair)
print("\n")
"""
   item no._x category_x  name_x  item no._y category_y      name_y
0           1  vegetable  carrot           4  vegetable       gourd
1           2  vegetable   beans           5      fruit       mango
2           3      fruit   apple           6      fruit       peach
3           4  vegetable  potato           7  vegetable        peas
4           5      fruit  grapes           8      fruit  watermelon
"""
new3_xdataflair = pd.merge(
    a, b,  right_index=True, how='inner', left_index=True)
print(new3_xdataflair)
print("\n")
"""
   item no._x category_x  name_x  item no._y category_y      name_y
0           1  vegetable  carrot           4  vegetable       gourd
1           2  vegetable   beans           5      fruit       mango
2           3      fruit   apple           6      fruit       peach
3           4  vegetable  potato           7  vegetable        peas
4           5      fruit  grapes           8      fruit  watermelon
"""


#RIGHT OUTER JOIN
new4_dataflair = pd.merge(a, b, on='item no.', how='right')
print(new4_dataflair)
print("\n")
"""
   item no. category_x  name_x category_y      name_y
0         4  vegetable  potato  vegetable       gourd
1         5      fruit  grapes      fruit       mango
2         6        NaN     NaN      fruit       peach
3         7        NaN     NaN  vegetable        peas
4         8        NaN     NaN      fruit  watermelon
"""


#LEFT OUTER JOIN
new4_dataflair = pd.merge(a, b, on='item no.', how='left')
print(new4_dataflair)
print("\n")
"""
   item no. category_x  name_x category_y name_y
0         1  vegetable  carrot        NaN    NaN
1         2  vegetable   beans        NaN    NaN
2         3      fruit   apple        NaN    NaN
3         4  vegetable  potato  vegetable  gourd
4         5      fruit  grapes      fruit  mango
=======
import numpy as np
import pandas as pd

dataflair = {
    'item no.': [1, 2, 3, 4, 5],
    'category': ['vegetable', 'vegetable', 'fruit', 'vegetable', 'fruit'],
    'name': ['carrot', 'beans', 'apple', 'potato', 'grapes']
}

a = pd.DataFrame(dataflair, columns=['item no.', 'category', 'name'])
print("DataFrame :\n", a)
"""
DataFrame :
    item no.   category    name
0         1  vegetable  carrot
1         2  vegetable   beans
2         3      fruit   apple
3         4  vegetable  potato
4         5      fruit  grapes

"""

dataflair2 = {
    'item no.': [4, 5, 6, 7, 8],
    'category': ['vegetable', 'fruit', 'fruit', 'vegetable', 'fruit'],
    'name': ['gourd', 'mango', 'peach', 'peas', 'watermelon']
}

b = pd.DataFrame(dataflair2, columns=['item no.', 'category', 'name'])
print("DataFrame :\n", b)
"""
DataFrame :
    item no.   category        name
0         4  vegetable       gourd
1         5      fruit       mango
2         6      fruit       peach
3         7  vegetable        peas
4         8      fruit  watermelon
"""

dataflair3 = {
       'item no.':[1,2,3,4,5,6,7,8,9,10],
        'price':[12,23,98,15,88,24,67,58,26,96]
}

c = pd.DataFrame(dataflair3, columns=['item no.', 'price'])
print("DataFrame :\n", c)
"""
DataFrame :
    item no.  price
0         1     12
1         2     23
2         3     98
3         4     15
4         5     88
5         6     24
6         7     67
7         8     58
8         9     26
9        10     96
"""

#PANDAS CONCATENATION

new_vdataflair=pd.concat([a,b])
print(new_vdataflair)
print("\n")
"""
   item no.   category        name
0         1  vegetable      carrot
1         2  vegetable       beans
2         3      fruit       apple
3         4  vegetable      potato
4         5      fruit      grapes
0         4  vegetable       gourd
1         5      fruit       mango
2         6      fruit       peach
3         7  vegetable        peas
4         8      fruit  watermelon
"""

#This gives us a DataFrame, with a and b together. 
# But this is vertical; to add horizontally, we use the following function:

new_hdataflair = pd.concat([a, b], axis=1)
print(new_hdataflair)
print("\n")
"""
   item no.   category    name  item no.   category        name
0         1  vegetable  carrot         4  vegetable       gourd
1         2  vegetable   beans         5      fruit       mango
2         3      fruit   apple         6      fruit       peach
3         4  vegetable  potato         7  vegetable        peas
4         5      fruit  grapes         8      fruit  watermelon
"""

#PANDAS MERGE
dataflair_x=pd.merge(new_vdataflair, c, on='item no.')
print(dataflair_x)
print("\n")
"""
   item no.   category        name  price
0         1  vegetable      carrot     12
1         2  vegetable       beans     23
2         3      fruit       apple     98
3         4  vegetable      potato     15
4         4  vegetable       gourd     15
5         5      fruit      grapes     88
6         5      fruit       mango     88
7         6      fruit       peach     24
8         7  vegetable        peas     67
9         8      fruit  watermelon     58
"""

#Pandas merging on multiple columns
dataflair_mkeys = pd.merge(a, b, on=['item no.', 'category'])
print(dataflair_mkeys)
print("\n")
"""
   item no.   category  name_x name_y
0         4  vegetable  potato  gourd
1         5      fruit  grapes  mango
"""

#Pandas merging on basis of index
"""
DataFrame :
    item no.   category    name
0         1  vegetable  carrot
1         2  vegetable   beans
2         3      fruit   apple
3         4  vegetable  potato
4         5      fruit  grapes
DataFrame :
    item no.   category        name
0         4  vegetable       gourd
1         5      fruit       mango
2         6      fruit       peach
3         7  vegetable        peas
4         8      fruit  watermelon
"""
new6_dataflair = pd.merge(a, b, right_index=True, left_index=True)
print(new6_dataflair)
print("\n")
"""
  item no._x category_x  name_x  item no._y category_y      name_y
0           1  vegetable  carrot           4  vegetable       gourd
1           2  vegetable   beans           5      fruit       mango
2           3      fruit   apple           6      fruit       peach
3           4  vegetable  potato           7  vegetable        peas
4           5      fruit  grapes           8      fruit  watermelon

"""


#PANDAS OUTER JOIN
new2_dataflair = pd.merge(a, b, on='item no.', how='outer')
print(new2_dataflair)
print("\n")
"""
   item no. category_x  name_x category_y      name_y
0         1  vegetable  carrot        NaN         NaN
1         2  vegetable   beans        NaN         NaN
2         3      fruit   apple        NaN         NaN
3         4  vegetable  potato  vegetable       gourd
4         5      fruit  grapes      fruit       mango
5         6        NaN     NaN      fruit       peach
6         7        NaN     NaN  vegetable        peas
7         8        NaN     NaN      fruit  watermelon
"""

#PANDAS INNER JOIN
new3_dataflair = pd.merge(a, b, on='item no.', how='inner')
print(new3_dataflair)
print("\n")
"""
  item no. category_x  name_x category_y name_y
0         4  vegetable  potato  vegetable  gourd
1         5      fruit  grapes      fruit  mango
"""
new3_xdataflair = pd.merge(a, b, on='item no.', how='inner', right_index=True, left_index=True)
print(new3_xdataflair)
print("\n")
"""
   item no. category_x  name_x category_y      name_y
0         1  vegetable  carrot  vegetable       gourd
1         2  vegetable   beans      fruit       mango
2         3      fruit   apple      fruit       peach
3         4  vegetable  potato  vegetable        peas
4         5      fruit  grapes      fruit  watermelon
"""
new3_xdataflair = pd.merge(
    a, b,  right_index=True, left_index=True)
print(new3_xdataflair)
print("\n")
"""
   item no._x category_x  name_x  item no._y category_y      name_y
0           1  vegetable  carrot           4  vegetable       gourd
1           2  vegetable   beans           5      fruit       mango
2           3      fruit   apple           6      fruit       peach
3           4  vegetable  potato           7  vegetable        peas
4           5      fruit  grapes           8      fruit  watermelon
"""
new3_xdataflair = pd.merge(
    a, b,  right_index=True, how='inner', left_index=True)
print(new3_xdataflair)
print("\n")
"""
   item no._x category_x  name_x  item no._y category_y      name_y
0           1  vegetable  carrot           4  vegetable       gourd
1           2  vegetable   beans           5      fruit       mango
2           3      fruit   apple           6      fruit       peach
3           4  vegetable  potato           7  vegetable        peas
4           5      fruit  grapes           8      fruit  watermelon
"""


#RIGHT OUTER JOIN
new4_dataflair = pd.merge(a, b, on='item no.', how='right')
print(new4_dataflair)
print("\n")
"""
   item no. category_x  name_x category_y      name_y
0         4  vegetable  potato  vegetable       gourd
1         5      fruit  grapes      fruit       mango
2         6        NaN     NaN      fruit       peach
3         7        NaN     NaN  vegetable        peas
4         8        NaN     NaN      fruit  watermelon
"""


#LEFT OUTER JOIN
new4_dataflair = pd.merge(a, b, on='item no.', how='left')
print(new4_dataflair)
print("\n")
"""
   item no. category_x  name_x category_y name_y
0         1  vegetable  carrot        NaN    NaN
1         2  vegetable   beans        NaN    NaN
2         3      fruit   apple        NaN    NaN
3         4  vegetable  potato  vegetable  gourd
4         5      fruit  grapes      fruit  mango
"""