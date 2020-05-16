import numpy as np
import pandas as pd


df = pd.read_excel("E:/Github/DataScience/Data-Science-Projects/Practice-assignments/DataFlair/sales_transactions.xlsx")
print(df)
"""
    Sno  account           name  order       sku  quantity  unit price  ext price
0     0   383080       Will LLC  10001  B1-20000         7       33.69     235.83
1     1   383080       Will LLC  10001  S1-27722        11       21.12     232.32
2     2   383080       Will LLC  10001  B1-86481         3       35.99     107.97
3     3   412290  Jerde-Hilpert  10005  S1-06532        48       55.82    2679.36
4     4   412290  Jerde-Hilpert  10005  S1-82801        21       13.62     286.02
5     5   412290  Jerde-Hilpert  10005  S1-06532         9       92.55     832.95
6     6   412290  Jerde-Hilpert  10005  S1-47412        44       78.91    3472.04
7     7   412290  Jerde-Hilpert  10005  S1-27722        36       25.42     915.12
8     8   218895      Kulas Inc  10006  S1-27722        32       95.66    3061.12
9     9   218895      Kulas Inc  10006  B1-33087        23       22.55     518.65
10   10   218895      Kulas Inc  10006  B1-33364         3       72.30     216.90
11   11   218895      Kulas Inc  10006  B1-20000        -1       72.18     -72.18
"""

"""
The question we would like to answer is: “What percentage of the order total does each sku represent?”
"""

"""
Approach 1 - Merging
"""

print("\n")
order_total = df.groupby("order")["ext price"].sum()
print(order_total)
"""
order
10001     576.12
10005    8185.49
10006    3724.49
Name: ext price, dtype: float64

"""
print(type(order_total))


order_total=order_total.rename('Order_Total')
print("\n")
print(order_total)
print(type(order_total))

order_total = order_total.reset_index()
print("\n")
print(order_total)
print(type(order_total))

df=df.merge(order_total)

print(df)

"""
   Sno  account           name  order       sku  quantity  unit price  ext price  Order_Total
0     0   383080       Will LLC  10001  B1-20000         7       33.69     235.83       576.12
1     1   383080       Will LLC  10001  S1-27722        11       21.12     232.32       576.12
2     2   383080       Will LLC  10001  B1-86481         3       35.99     107.97       576.12
3     3   412290  Jerde-Hilpert  10005  S1-06532        48       55.82    2679.36      8185.49
4     4   412290  Jerde-Hilpert  10005  S1-82801        21       13.62     286.02      8185.49
5     5   412290  Jerde-Hilpert  10005  S1-06532         9       92.55     832.95      8185.49
6     6   412290  Jerde-Hilpert  10005  S1-47412        44       78.91    3472.04      8185.49
7     7   412290  Jerde-Hilpert  10005  S1-27722        36       25.42     915.12      8185.49
8     8   218895      Kulas Inc  10006  S1-27722        32       95.66    3061.12      3724.49
9     9   218895      Kulas Inc  10006  B1-33087        23       22.55     518.65      3724.49
10   10   218895      Kulas Inc  10006  B1-33364         3       72.30     216.90      3724.49
11   11   218895      Kulas Inc  10006  B1-20000        -1       72.18     -72.18      3724.49
"""

"""
Approach 2  - Using Transform
"""

df['Order_Total']=df.groupby('order')['ext price'].transform('sum')
print(df)

"""
   Sno  account           name  order       sku  quantity  unit price  ext price  Order_Total
0     0   383080       Will LLC  10001  B1-20000         7       33.69     235.83       576.12
1     1   383080       Will LLC  10001  S1-27722        11       21.12     232.32       576.12
2     2   383080       Will LLC  10001  B1-86481         3       35.99     107.97       576.12
3     3   412290  Jerde-Hilpert  10005  S1-06532        48       55.82    2679.36      8185.49
4     4   412290  Jerde-Hilpert  10005  S1-82801        21       13.62     286.02      8185.49
5     5   412290  Jerde-Hilpert  10005  S1-06532         9       92.55     832.95      8185.49
6     6   412290  Jerde-Hilpert  10005  S1-47412        44       78.91    3472.04      8185.49
7     7   412290  Jerde-Hilpert  10005  S1-27722        36       25.42     915.12      8185.49
8     8   218895      Kulas Inc  10006  S1-27722        32       95.66    3061.12      3724.49
9     9   218895      Kulas Inc  10006  B1-33087        23       22.55     518.65      3724.49
10   10   218895      Kulas Inc  10006  B1-33364         3       72.30     216.90      3724.49
11   11   218895      Kulas Inc  10006  B1-20000        -1       72.18     -72.18      3724.49

=======
import numpy as np
import pandas as pd


df = pd.read_excel("E:/Github/DataScience/Data-Science-Projects/Practice-assignments/DataFlair/sales_transactions.xlsx")
print(df)
"""
    Sno  account           name  order       sku  quantity  unit price  ext price
0     0   383080       Will LLC  10001  B1-20000         7       33.69     235.83
1     1   383080       Will LLC  10001  S1-27722        11       21.12     232.32
2     2   383080       Will LLC  10001  B1-86481         3       35.99     107.97
3     3   412290  Jerde-Hilpert  10005  S1-06532        48       55.82    2679.36
4     4   412290  Jerde-Hilpert  10005  S1-82801        21       13.62     286.02
5     5   412290  Jerde-Hilpert  10005  S1-06532         9       92.55     832.95
6     6   412290  Jerde-Hilpert  10005  S1-47412        44       78.91    3472.04
7     7   412290  Jerde-Hilpert  10005  S1-27722        36       25.42     915.12
8     8   218895      Kulas Inc  10006  S1-27722        32       95.66    3061.12
9     9   218895      Kulas Inc  10006  B1-33087        23       22.55     518.65
10   10   218895      Kulas Inc  10006  B1-33364         3       72.30     216.90
11   11   218895      Kulas Inc  10006  B1-20000        -1       72.18     -72.18
"""

"""
The question we would like to answer is: “What percentage of the order total does each sku represent?”
"""

"""
Approach 1 - Merging
"""

print("\n")
order_total = df.groupby("order")["ext price"].sum()
print(order_total)
"""
order
10001     576.12
10005    8185.49
10006    3724.49
Name: ext price, dtype: float64

"""
print(type(order_total))


order_total=order_total.rename('Order_Total')
print("\n")
print(order_total)
print(type(order_total))

order_total = order_total.reset_index()
print("\n")
print(order_total)
print(type(order_total))

df=df.merge(order_total)

print(df)

"""
   Sno  account           name  order       sku  quantity  unit price  ext price  Order_Total
0     0   383080       Will LLC  10001  B1-20000         7       33.69     235.83       576.12
1     1   383080       Will LLC  10001  S1-27722        11       21.12     232.32       576.12
2     2   383080       Will LLC  10001  B1-86481         3       35.99     107.97       576.12
3     3   412290  Jerde-Hilpert  10005  S1-06532        48       55.82    2679.36      8185.49
4     4   412290  Jerde-Hilpert  10005  S1-82801        21       13.62     286.02      8185.49
5     5   412290  Jerde-Hilpert  10005  S1-06532         9       92.55     832.95      8185.49
6     6   412290  Jerde-Hilpert  10005  S1-47412        44       78.91    3472.04      8185.49
7     7   412290  Jerde-Hilpert  10005  S1-27722        36       25.42     915.12      8185.49
8     8   218895      Kulas Inc  10006  S1-27722        32       95.66    3061.12      3724.49
9     9   218895      Kulas Inc  10006  B1-33087        23       22.55     518.65      3724.49
10   10   218895      Kulas Inc  10006  B1-33364         3       72.30     216.90      3724.49
11   11   218895      Kulas Inc  10006  B1-20000        -1       72.18     -72.18      3724.49
"""

"""
Approach 2  - Using Transform
"""

df['Order_Total']=df.groupby('order')['ext price'].transform('sum')
print(df)

"""
   Sno  account           name  order       sku  quantity  unit price  ext price  Order_Total
0     0   383080       Will LLC  10001  B1-20000         7       33.69     235.83       576.12
1     1   383080       Will LLC  10001  S1-27722        11       21.12     232.32       576.12
2     2   383080       Will LLC  10001  B1-86481         3       35.99     107.97       576.12
3     3   412290  Jerde-Hilpert  10005  S1-06532        48       55.82    2679.36      8185.49
4     4   412290  Jerde-Hilpert  10005  S1-82801        21       13.62     286.02      8185.49
5     5   412290  Jerde-Hilpert  10005  S1-06532         9       92.55     832.95      8185.49
6     6   412290  Jerde-Hilpert  10005  S1-47412        44       78.91    3472.04      8185.49
7     7   412290  Jerde-Hilpert  10005  S1-27722        36       25.42     915.12      8185.49
8     8   218895      Kulas Inc  10006  S1-27722        32       95.66    3061.12      3724.49
9     9   218895      Kulas Inc  10006  B1-33087        23       22.55     518.65      3724.49
10   10   218895      Kulas Inc  10006  B1-33364         3       72.30     216.90      3724.49
11   11   218895      Kulas Inc  10006  B1-20000        -1       72.18     -72.18      3724.49

"""