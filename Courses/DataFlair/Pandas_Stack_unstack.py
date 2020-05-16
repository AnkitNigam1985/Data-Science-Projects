import numpy as np
import pandas as pd

#Using multiindex for dataframe header rather than index of the dataframe
header = pd.MultiIndex.from_product( [['Semester1', 'Semester2'], ['Maths', 'Science']])
d = ([[12, 45, 67, 56], [78, 89, 45, 67], [45, 67, 89, 90], [67, 44, 56, 55]])


df = pd.DataFrame(d,
                  index=['Alisa', 'Bobby', 'Cathrine', 'Jack'],
                  columns=header)
print("\nOriginal dataframe :\n", df)

"""
Original dataframe :
            Semester1         Semester2
             Maths Science     Maths Science
Alisa           12      45        67      56
Bobby           78      89        45      67
Cathrine        45      67        89      90
Jack            67      44        56      55
"""

#Stack the dataframe
stacked_df1 = df.stack()
print("\nStacked Dataframe from original :\n", stacked_df1)

#Again stacked further
stacked_df2 = stacked_df1.stack()
print("\nFurther Stacked Dataframe from original  :\n", stacked_df2)

#Unstack the dataframe
unstacked_df1 = df.unstack()
print("Unstacked Dataframe from original :\n", unstacked_df1)

#Unstack the dataframe
unstacked_df2 = unstacked_df1.unstack()
print("Further Unstacked Dataframe from original :\n", unstacked_df2)


#Unstack the stacked dataframe
unstacked_df3 = stacked_df1.unstack()
print("Unstacked Dataframe from Stacked one :\n", unstacked_df3)


#Stack the original dataframe at level=0
print("\nOriginal dataframe :\n", df)
#Stack at level=0
stacked_dflvl0 = df.stack(level=0)
print("\nStacked Dataframe at level=0 from original  :\n", stacked_dflvl0)
#Unstack it
unstacked_df_stacked_lvl0 = stacked_dflvl0.unstack()
print("\nUnStacked Dataframe which is stacked at level=0  :\n", unstacked_df_stacked_lvl0)


#Stack the original dataframe at level=1
print("\nOriginal dataframe :\n", df)
#Stack at level=0
stacked_dflvl1 = df.stack(level=1)
print("\nStacked Dataframe at level=1 from original  :\n", stacked_dflvl1)
#Unstack it
unstacked_df_stacked_lvl1 = stacked_dflvl1.unstack()
print("\nUnStacked Dataframe which is stacked at level=1  :\n",  unstacked_df_stacked_lvl1)

=======
import numpy as np
import pandas as pd

#Using multiindex for dataframe header rather than index of the dataframe
header = pd.MultiIndex.from_product( [['Semester1', 'Semester2'], ['Maths', 'Science']])
d = ([[12, 45, 67, 56], [78, 89, 45, 67], [45, 67, 89, 90], [67, 44, 56, 55]])


df = pd.DataFrame(d,
                  index=['Alisa', 'Bobby', 'Cathrine', 'Jack'],
                  columns=header)
print("\nOriginal dataframe :\n", df)

"""
Original dataframe :
            Semester1         Semester2
             Maths Science     Maths Science
Alisa           12      45        67      56
Bobby           78      89        45      67
Cathrine        45      67        89      90
Jack            67      44        56      55
"""

#Stack the dataframe
stacked_df1 = df.stack()
print("\nStacked Dataframe from original :\n", stacked_df1)

#Again stacked further
stacked_df2 = stacked_df1.stack()
print("\nFurther Stacked Dataframe from original  :\n", stacked_df2)

#Unstack the dataframe
unstacked_df1 = df.unstack()
print("Unstacked Dataframe from original :\n", unstacked_df1)

#Unstack the dataframe
unstacked_df2 = unstacked_df1.unstack()
print("Further Unstacked Dataframe from original :\n", unstacked_df2)


#Unstack the stacked dataframe
unstacked_df3 = stacked_df1.unstack()
print("Unstacked Dataframe from Stacked one :\n", unstacked_df3)


#Stack the original dataframe at level=0
print("\nOriginal dataframe :\n", df)
#Stack at level=0
stacked_dflvl0 = df.stack(level=0)
print("\nStacked Dataframe at level=0 from original  :\n", stacked_dflvl0)
#Unstack it
unstacked_df_stacked_lvl0 = stacked_dflvl0.unstack()
print("\nUnStacked Dataframe which is stacked at level=0  :\n", unstacked_df_stacked_lvl0)


#Stack the original dataframe at level=1
print("\nOriginal dataframe :\n", df)
#Stack at level=0
stacked_dflvl1 = df.stack(level=1)
print("\nStacked Dataframe at level=1 from original  :\n", stacked_dflvl1)
#Unstack it
unstacked_df_stacked_lvl1 = stacked_dflvl1.unstack()
print("\nUnStacked Dataframe which is stacked at level=1  :\n",  unstacked_df_stacked_lvl1)

