import numpy as np
import pandas as pd
import datetime

#How to create Pandas datetime object?
"""
To create Pandas DateTime object we use the .date_range function. It has the following parameter:

    First parameter: start= ‘dd/mm/yyyy’.
    Second parameter: periods= n, where n is no of periods or date time elements you need.
    Third parameter: freq= ‘x’, where ‘x’ can be ‘H’(hour), ‘D’(days), ‘W’(weeks), ‘M’(month), ‘Y’(years), etc.
"""
dataflair = pd.date_range(start='1/1/2011', periods=10, freq='H')
print(dataflair)
print("\n")
"""
DatetimeIndex(['2011-01-01 00:00:00', '2011-01-01 01:00:00',
               '2011-01-01 02:00:00', '2011-01-01 03:00:00',
               '2011-01-01 04:00:00', '2011-01-01 05:00:00',
               '2011-01-01 06:00:00', '2011-01-01 07:00:00',
               '2011-01-01 08:00:00', '2011-01-01 09:00:00'],
              dtype='datetime64[ns]', freq='H')
"""
print(pd.date_range(start='1/1/2011', periods=10, freq='W'))
print("\n")
"""
DatetimeIndex(['2011-01-02', '2011-01-09', '2011-01-16', '2011-01-23',
               '2011-01-30', '2011-02-06', '2011-02-13', '2011-02-20',
               '2011-02-27', '2011-03-06'],
              dtype='datetime64[ns]', freq='W-SUN')
"""


#How to print date in yyyy-mm-dd format
dataflair_rng = pd.DataFrame() 
dataflair_rng['date'] = pd.date_range('1/1/2011', periods=72, freq='H')
print(dataflair_rng[:5])
print("\n")
"""
                date
0 2011-01-01 00:00:00
1 2011-01-01 01:00:00
2 2011-01-01 02:00:00
3 2011-01-01 03:00:00
4 2011-01-01 04:00:00

"""

#Breaking the time and date into separate features

# creates ‘year’ column and extracts year
dataflair_rng['year'] = dataflair_rng['date'].dt.year
print(dataflair_rng['year'])
print("\n")
"""
0     2011
1     2011
2     2011
3     2011
4     2011
      ...
67    2011
68    2011
69    2011
70    2011
71    2011
Name: year, Length: 72, dtype: int64
"""


# creates ‘month’ column and extracts month
dataflair_rng['month'] = dataflair_rng['date'].dt.month
print(dataflair_rng['month'])
print("\n")
"""
0     1
1     1
2     1
3     1
4     1
     ..
67    1
68    1
69    1
70    1
71    1
Name: month, Length: 72, dtype: int64
"""



# creates ‘day’ column and extracts day
dataflair_rng['day'] = dataflair_rng['date'].dt.day
print(dataflair_rng['day'])
print("\n")
"""
0     1
1     1
2     1
3     1
4     1
     ..
67    3
68    3
69    3
70    3
71    3
Name: day, Length: 72, dtype: int64
"""

# creates ‘hour’ column and extracts hour
dataflair_rng['hour'] = dataflair_rng['date'].dt.hour
print(dataflair_rng['hour'])
print("\n")
"""
0      0
1      1
2      2
3      3
4      4
      ..
67    19
68    20
69    21
70    22
71    23
Name: hour, Length: 72, dtype: int64
"""

# creates ‘minute’ column and extracts minute
dataflair_rng['minute'] = dataflair_rng['date'].dt.minute
print(dataflair_rng['minute'])
print("\n")
"""
0     0
1     0
2     0
3     0
4     0
     ..
67    0
68    0
69    0
70    0
71    0
Name: minute, Length: 72, dtype: int64
"""

print(dataflair_rng.head(3))
print("\n")
"""
                 date  year  month  day  hour  minute
0 2011-01-01 00:00:00  2011      1    1     0       0
1 2011-01-01 01:00:00  2011      1    1     1       0
2 2011-01-01 02:00:00  2011      1    1     2       0
"""

#Getting current TimeStamp
dataflair_time = pd.Timestamp.now()
print(dataflair_time)
print("\n")
"""
2020-01-02 13:53:37.693493
"""

#Getting all the features separately from TimeStamp
print(dataflair_time.year)
print("\n")
#2020

print(dataflair_time.month)
print("\n")
#1

print(dataflair_time.day)
print("\n")
#2

print(dataflair_time.hour)
print("\n")
#13

print(dataflair_time.minute)
print("\n")
#57

print(dataflair_time.second)
print("\n")
#33

print(dataflair_time.weekday())
print("\n")
#3


dataflair_dx = pd.date_range(
    start='2000-01-10 06:30', freq='W', periods=3, tz='Asia/Calcutta')
print(dataflair_dx)
print("\n")
"""
DatetimeIndex(['2000-01-16 06:30:00+05:30', '2000-01-23 06:30:00+05:30',
               '2000-01-30 06:30:00+05:30'],
              dtype='datetime64[ns, Asia/Calcutta]', freq='W-SUN')

"""
#Getting all the features separately from TimeStamp
print(dataflair_dx.year)
print("\n")
#Int64Index([2000, 2000, 2000], dtype='int64')

print(dataflair_dx.month)
print("\n")
#Int64Index([1, 1, 1], dtype='int64')

print(dataflair_dx.day)
print("\n")
#Int64Index([16, 23, 30], dtype='int64')

print(dataflair_dx.hour)
print("\n")
#Int64Index([6, 6, 6], dtype='int64')

print(dataflair_dx.minute)
print("\n")
#Int64Index([30, 30, 30], dtype='int64')

print(dataflair_dx.second)
print("\n")
#Int64Index([0, 0, 0], dtype='int64')

print(dataflair_dx.weekday)
print("\n")
#Int64Index([6, 6, 6], dtype='int64')


#PANDAS TIME DELTA
dataflair_time = pd.Timedelta('17 days 7 hours 45 minutes 56 seconds')
print(dataflair_time)
print("\n")
#17 days 07:45:56


dataflair_time2= pd.Timedelta(19,unit='h')
print(dataflair_time2)
print("\n")
#0 days 19:00:00

dataflair_time3 = pd.Timedelta(39, unit='h')
print(dataflair_time3)
print("\n")
#1 days 15:00:00


dataflair_time4 = pd.Timedelta(days=9, minutes=45)
print(dataflair_time4)
print("\n")
#9 days 00:45:00


#PANDAS TIME SERIES
dataflair_dict = {'date': ['2018-06-02 12:30:04', '2018-07-02 01:27:03', '2018-07-15 17:23:12', '2018-07-30 05:34:05', '2018-08-04 19:17:23', '2018-08-12 03:12:34',
                           '2018-09-03 09:42:05', '2018-09-03 15:54:08', '2018-09-04 18:47:16', '2018-09-04 17:37:25'], 'Sales': [134, 225, 216, 65, 15, 114, 236, 215, 92, 61]}
print(dataflair_dict)
print("\n")
"""
{'date': ['2018-06-02 12:30:04', '2018-07-02 01:27:03', '2018-07-15 17:23:12', '2018-07-30 05:34:05', '2018-08-04 19:17:23', '2018-08-12 03:12:34', '2018-09-03 09:42:05', '2018-09-03 15:54:08', '2018-09-04 18:47:16', '2018-09-04 17:37:25'], 
'Sales': [134, 225, 216, 65, 15, 114, 236, 215, 92, 61]}
"""

dataflair_df = pd.DataFrame(dataflair_dict, columns = ['date', 'Sales'])
print(dataflair_df)
print("\n")
"""
                  date  Sales
0  2018-06-02 12:30:04    134
1  2018-07-02 01:27:03    225
2  2018-07-15 17:23:12    216
3  2018-07-30 05:34:05     65
4  2018-08-04 19:17:23     15
5  2018-08-12 03:12:34    114
6  2018-09-03 09:42:05    236
7  2018-09-03 15:54:08    215
8  2018-09-04 18:47:16     92
9  2018-09-04 17:37:25     61

"""
#How to convert the dates to a TimeSeries object in Pandas?
dataflair_df['date'] = pd.to_datetime(dataflair_df['date'])
dataflair_df.index = dataflair_df['date']
del dataflair_df['date']
print(dataflair_df)
print("\n")
"""
                        Sales
date
2018-06-02 12:30:04    134
2018-07-02 01:27:03    225
2018-07-15 17:23:12    216
2018-07-30 05:34:05     65
2018-08-04 19:17:23     15
2018-08-12 03:12:34    114
2018-09-03 09:42:05    236
2018-09-03 15:54:08    215
2018-09-04 18:47:16     92
2018-09-04 17:37:25     61

"""

print(dataflair_df['2018-08'])  #to get entries for year-2018 and month=08 in index
"""
                     Sales
date
2018-08-04 19:17:23     15
2018-08-12 03:12:34    114
"""

print(dataflair_df.index)
"""
DatetimeIndex(['2018-06-02 12:30:04', '2018-07-02 01:27:03',
               '2018-07-15 17:23:12', '2018-07-30 05:34:05',
               '2018-08-04 19:17:23', '2018-08-12 03:12:34',
               '2018-09-03 09:42:05', '2018-09-03 15:54:08',
               '2018-09-04 18:47:16', '2018-09-04 17:37:25'],
              dtype='datetime64[ns]', name='date', freq=None)
"""
