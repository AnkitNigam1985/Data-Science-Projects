import numpy as np
import pandas as pd

#Create a DataFrame
d = {
    'Name': ['Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine',
             'Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine'],
    'Exam': ['Semester 1', 'Semester 1', 'Semester 1', 'Semester 1', 'Semester 1', 'Semester 1',
             'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2'],

    'Subject': ['Mathematics', 'Mathematics', 'Mathematics', 'Science', 'Science', 'Science',
                'Mathematics', 'Mathematics', 'Mathematics', 'Science', 'Science', 'Science'],
    'Result': ['Pass', 'Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail', 'Fail', 'Pass', 'Pass', 'Fail']}

df = pd.DataFrame(d, columns=['Name', 'Exam', 'Subject', 'Result'])
print("\nOriginal DataFrame :\n", df)

"""
Original DataFrame :
         Name        Exam      Subject Result
0      Alisa  Semester 1  Mathematics   Pass
1      Bobby  Semester 1  Mathematics   Pass
2   Cathrine  Semester 1  Mathematics   Fail
3      Alisa  Semester 1      Science   Pass
4      Bobby  Semester 1      Science   Fail
5   Cathrine  Semester 1      Science   Pass
6      Alisa  Semester 2  Mathematics   Pass
7      Bobby  Semester 2  Mathematics   Fail
8   Cathrine  Semester 2  Mathematics   Fail
9      Alisa  Semester 2      Science   Pass
10     Bobby  Semester 2      Science   Pass
11  Cathrine  Semester 2      Science   Fail
"""


# 2 way cross table

print("\n2-way crosstable :\n", pd.crosstab(df.Subject, df.Result, margins=True))

"""
2-way crosstable :
 Result       Fail  Pass  All
Subject
Mathematics     3     3    6
Science         2     4    6
All             5     7   12
"""


# 3 way cross table

print("\n3-way crosstable :\n", pd.crosstab([df.Subject, df.Exam], df.Result, margins=True))
"""
3-way crosstable :
 Result                  Fail  Pass  All
Subject     Exam
Mathematics Semester 1     1     2    3
            Semester 2     2     1    3
Science     Semester 1     1     2    3
            Semester 2     1     2    3
All                        5     7   12

"""