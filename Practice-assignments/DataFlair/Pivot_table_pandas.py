import numpy as np
import pandas as pd


#PIVOT TABLE - the fields provided in index field are index 
# and all the operations would be carried on remaining fields
#Create a DataFrame
d = {
    'Name': ['Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine',
             'Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine'],
    'Exam': ['Semester 1', 'Semester 1', 'Semester 1', 'Semester 1', 'Semester 1', 'Semester 1',
             'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2'],

    'Subject': ['Mathematics', 'Mathematics', 'Mathematics', 'Science', 'Science', 'Science',
                'Mathematics', 'Mathematics', 'Mathematics', 'Science', 'Science', 'Science'],
    'Score': [62, 47, 55, 74, 31, 77, 85, 63, 42, 67, 89, 81]}

df = pd.DataFrame(d)
print(df)
"""
        Name        Exam      Subject  Score
0      Alisa  Semester 1  Mathematics     62
1      Bobby  Semester 1  Mathematics     47
2   Cathrine  Semester 1  Mathematics     55
3      Alisa  Semester 1      Science     74
4      Bobby  Semester 1      Science     31
5   Cathrine  Semester 1      Science     77
6      Alisa  Semester 2  Mathematics     85
7      Bobby  Semester 2  Mathematics     63
8   Cathrine  Semester 2  Mathematics     42
9      Alisa  Semester 2      Science     67
10     Bobby  Semester 2      Science     89
11  Cathrine  Semester 2      Science     81
"""
# pivot table using aggregate function mean

print(pd.pivot_table(df, index=['Exam', 'Subject'], aggfunc='mean'))
"""
                          Score
Exam       Subject
Semester 1 Mathematics  54.666667
           Science      60.666667
Semester 2 Mathematics  63.333333
           Science      79.000000
"""
#No name column above as it is non-numeric so can't get mean

# pivot table using aggregate function sum

print(pd.pivot_table(df, index=['Name', 'Subject'], aggfunc='sum'))

"""
                      Score
Name     Subject
Alisa    Mathematics    147
         Science        141
Bobby    Mathematics    110
         Science        120
Cathrine Mathematics     97
         Science        158
"""
#No name column above as it is non-numeric so can't get sum


# pivot table using aggregate function count

print(pd.pivot_table(df, index=['Exam', 'Subject'], aggfunc='count'))
"""
                      Name  Score
Exam       Subject
Semester 1 Mathematics     3      3
           Science         3      3
Semester 2 Mathematics     3      3
           Science         3      3

"""
#name column now present as we can get count of categorical column also

print(pd.pivot_table(df, values='Score', index='Name', columns='Subject' ))
"""
Subject   Mathematics  Science
Name
Alisa            73.5     70.5
Bobby            55.0     60.0
Cathrine         48.5     79.0

"""
#operation on values field