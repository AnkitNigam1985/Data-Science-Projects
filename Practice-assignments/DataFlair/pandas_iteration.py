import numpy as np
import pandas as pd


dataflair = pd.read_csv(
    "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")

print(dataflair)
"""
   Month   "1958"   "1959"   "1960"
0    JAN      340      360      417
1    FEB      318      342      391
2    MAR      362      406      419
3    APR      348      396      461
4    MAY      363      420      472
5    JUN      435      472      535
6    JUL      491      548      622
7    AUG      505      559      606
8    SEP      404      463      508
9    OCT      359      407      461
10   NOV      310      362      390
11   DEC      337      405      432
"""

#iteritems() in Pandas
"""
Helps to iterate over each element of the set, column-wise.
The function iteritems() lets us travel and visit each and every value of the dataset.
"""

print("iteritems() in pandas:\n")
for key, values in dataflair.iteritems():
    print(key, values)
print("\n")
"""
iteritems() in pandas:

    Month 
0     JAN
1     FEB
2     MAR
3     APR
4     MAY
5     JUN
6     JUL
7     AUG
8     SEP
9     OCT
10    NOV
11    DEC
Name: Month, dtype: object
    "1958" 
0     340
1     318
2     362
3     348
4     363
5     435
6     491
7     505
8     404
9     359
10    310
11    337
Name:  "1958", dtype: int64
    "1959" 
0     360
1     342
2     406
3     396
4     420
5     472
6     548
7     559
8     463
9     407
10    362
11    405
Name:  "1959", dtype: int64
    "1960" 
0     417
1     391
2     419
3     461
4     472
5     535
6     622
7     606
8     508
9     461
10    390
11    432
Name:  "1960", dtype: int64
"""

#iterrows() in dataframe
"""
With iterrows() we can visit all the elements of a dataset, row-wise.

"""
print("\n")
for row_index, row in dataflair.iterrows():
    print(row_index, row)
print("\n")
"""
0 Month    JAN
 "1958"    340
 "1959"    360
 "1960"    417
Name: 0, dtype: object
1 Month    FEB
 "1958"    318
 "1959"    342
 "1960"    391
Name: 1, dtype: object
2 Month   	MAR
 "1958"    362
 "1959"    406
 "1960"    419
Name: 2, dtype: object
3 Month    APR
 "1958"    348
 "1959"    396
 "1960"    461
Name: 3, dtype: object
4 Month    MAY
 "1958"    363
 "1959"    420
 "1960"    472
Name: 4, dtype: object
5 Month    JUN
 "1958"    435
 "1959"    472
 "1960"    535
Name: 5, dtype: object
6 Month    JUL
 "1958"    491
 "1959"    548
 "1960"    622
Name: 6, dtype: object
7 Month    AUG
 "1958"    505
 "1959"    559
 "1960"    606
Name: 7, dtype: object
8 Month    SEP
 "1958"    404
 "1959"    463
 "1960"    508
Name: 8, dtype: object
9 Month    OCT
 "1958"    359
 "1959"    407
 "1960"    461
Name: 9, dtype: object
10 Month   NOV
 "1958"    310
 "1959"    362
 "1960"    390
Name: 10, dtype: object
11 Month   DEC
 "1958"    337
 "1959"    405
 "1960"    432
Name: 11, dtype: object
"""

#itertuples() 
"""
The function itertuples() creates a tuple for every row in the dataset. 
Thus iterating over it would give us a tuple of the rows present.
"""
for row in dataflair.itertuples():
    print(row)
"""
Pandas(Index=0, Month='JAN', _2=340, _3=360, _4=417)
Pandas(Index=1, Month='FEB', _2=318, _3=342, _4=391)
Pandas(Index=2, Month='MAR', _2=362, _3=406, _4=419)
Pandas(Index=3, Month='APR', _2=348, _3=396, _4=461)
Pandas(Index=4, Month='MAY', _2=363, _3=420, _4=472)
Pandas(Index=5, Month='JUN', _2=435, _3=472, _4=535)
Pandas(Index=6, Month='JUL', _2=491, _3=548, _4=622)
Pandas(Index=7, Month='AUG', _2=505, _3=559, _4=606)
Pandas(Index=8, Month='SEP', _2=404, _3=463, _4=508)
Pandas(Index=9, Month='OCT', _2=359, _3=407, _4=461)
Pandas(Index=10, Month='NOV', _2=310, _3=362, _4=390)
Pandas(Index=11, Month='DEC', _2=337, _3=405, _4=432)
"""

