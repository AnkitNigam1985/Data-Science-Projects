import numpy as np
import pandas as pd


dataflair_df = pd.read_excel(
    "E:/Github/DataScience/Data-Science-Projects/Practice-assignments/DataFlair/sales_transactions.xlsx")

print(dataflair_df.count())
"""
Sno           12
account       12
name          12
order         12
sku           12
quantity      12
unit price    12
ext price     12
dtype: int64

"""

print(dataflair_df[["account"]].count())
print("\n")
"""
account    12
dtype: int64
"""

print(dataflair_df.sum())
print("\n")
"""
Sno                                                          66
account                                                 4086270
name          Will LLCWill LLCWill LLCJerde-HilpertJerde-Hil...
order                                                    120052
sku           B1-20000S1-27722B1-86481S1-06532S1-82801S1-065...
quantity                                                    236
unit price                                               619.81
ext price                                               12486.1
dtype: object
"""

print(dataflair_df["unit price"].sum())
print("\n")
"""
619.81
"""
print(dataflair_df["unit price"].min())
print("\n")
"""
13.62
"""

print(dataflair_df["unit price"].max())
print("\n")
"""
95.66
"""

print(dataflair_df.min())
print("\n")
"""
Sno                       0
account              218895
name          Jerde-Hilpert
order                 10001
sku                B1-20000
quantity                 -1
unit price            13.62
ext price            -72.18
dtype: object
"""

print(dataflair_df.max())
print("\n")
"""
Sno                 11
account         412290
name          Will LLC
order            10006
sku           S1-82801
quantity            48
unit price       95.66
ext price      3472.04
dtype: object
"""

print(dataflair_df['ext price'].mean())
print("\n")
"""
1040.5083333333332
"""

print(dataflair_df['ext price'].median())
print("\n")
"""
402.335
"""

print(dataflair_df['ext price'].std())
print("\n")
"""
1267.3577868637738
"""

#GROUPING
print(dataflair_df.groupby("account").mean())
print("\n")
"""
         Sno    order  quantity  unit price  ext price
account
218895   9.5  10006.0     14.25   65.672500   931.1225
383080   1.0  10001.0      7.00   30.266667   192.0400
412290   5.0  10005.0     31.60   53.264000  1637.0980

"""

print(dataflair_df.groupby("account").aggregate(['min', 'max']))
print("\n")
"""
        Sno               name                 order              sku           quantity     unit price        ext price
        min max            min            max    min    max       min       max      min max        min    max       min      max
account
218895    8  11      Kulas Inc      Kulas Inc  10006  10006  B1-20000  S1-27722       -1  32      22.55  95.66    -72.18  3061.12
383080    0   2       Will LLC       Will LLC  10001  10001  B1-20000  S1-27722        3  11      21.12  35.99    107.97   235.83
412290    3   7  Jerde-Hilpert  Jerde-Hilpert  10005  10005  S1-06532  S1-82801        9  48      13.62  92.55    286.02  3472.04

"""
print(dataflair_df.groupby("account")['ext price'].aggregate(['min', 'max']))
print("\n")
"""
            min      max
account
218895   -72.18  3061.12
383080   107.97   235.83
412290   286.02  3472.04
"""

=======
import numpy as np
import pandas as pd


dataflair_df = pd.read_excel(
    "E:/Github/DataScience/Data-Science-Projects/Practice-assignments/DataFlair/sales_transactions.xlsx")

print(dataflair_df.count())
"""
Sno           12
account       12
name          12
order         12
sku           12
quantity      12
unit price    12
ext price     12
dtype: int64

"""

print(dataflair_df[["account"]].count())
print("\n")
"""
account    12
dtype: int64
"""

print(dataflair_df.sum())
print("\n")
"""
Sno                                                          66
account                                                 4086270
name          Will LLCWill LLCWill LLCJerde-HilpertJerde-Hil...
order                                                    120052
sku           B1-20000S1-27722B1-86481S1-06532S1-82801S1-065...
quantity                                                    236
unit price                                               619.81
ext price                                               12486.1
dtype: object
"""

print(dataflair_df["unit price"].sum())
print("\n")
"""
619.81
"""
print(dataflair_df["unit price"].min())
print("\n")
"""
13.62
"""

print(dataflair_df["unit price"].max())
print("\n")
"""
95.66
"""

print(dataflair_df.min())
print("\n")
"""
Sno                       0
account              218895
name          Jerde-Hilpert
order                 10001
sku                B1-20000
quantity                 -1
unit price            13.62
ext price            -72.18
dtype: object
"""

print(dataflair_df.max())
print("\n")
"""
Sno                 11
account         412290
name          Will LLC
order            10006
sku           S1-82801
quantity            48
unit price       95.66
ext price      3472.04
dtype: object
"""

print(dataflair_df['ext price'].mean())
print("\n")
"""
1040.5083333333332
"""

print(dataflair_df['ext price'].median())
print("\n")
"""
402.335
"""

print(dataflair_df['ext price'].std())
print("\n")
"""
1267.3577868637738
"""

#GROUPING
print(dataflair_df.groupby("account").mean())
print("\n")
"""
         Sno    order  quantity  unit price  ext price
account
218895   9.5  10006.0     14.25   65.672500   931.1225
383080   1.0  10001.0      7.00   30.266667   192.0400
412290   5.0  10005.0     31.60   53.264000  1637.0980

"""

print(dataflair_df.groupby("account").aggregate(['min', 'max']))
print("\n")
"""
        Sno               name                 order              sku           quantity     unit price        ext price
        min max            min            max    min    max       min       max      min max        min    max       min      max
account
218895    8  11      Kulas Inc      Kulas Inc  10006  10006  B1-20000  S1-27722       -1  32      22.55  95.66    -72.18  3061.12
383080    0   2       Will LLC       Will LLC  10001  10001  B1-20000  S1-27722        3  11      21.12  35.99    107.97   235.83
412290    3   7  Jerde-Hilpert  Jerde-Hilpert  10005  10005  S1-06532  S1-82801        9  48      13.62  92.55    286.02  3472.04

"""
print(dataflair_df.groupby("account")['ext price'].aggregate(['min', 'max']))
print("\n")
"""
            min      max
account
218895   -72.18  3061.12
383080   107.97   235.83
412290   286.02  3472.04
"""

