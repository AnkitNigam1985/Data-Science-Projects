import numpy as np
import pandas as pd


#Pandas.get_option()
"""
With the help of .get_option in pandas, we can define parameter which will give us a particular detail about the default values in pandas.
Using “display.max_rows” and “display.max_columns” as parameters we get a maximum number of rows and columns that can display by default.
"""
dataflair = pd.get_option("display.max_rows")
print(dataflair)
"""
60
"""

dataflair2 = pd.get_option("display.max_columns")
print(dataflair)
"""
60
"""

#Pandas.set_option()
"""
The .set_option() function allows us to change a default value to something of our choice. 
In the example given below, we see that we can change the “display.max_rows” from 60 to 90.
"""
pd.set_option("display.max_rows", 90)
dataflair3 = pd.get_option("display.max_rows")
print(dataflair3)
#90

pd.set_option("display.max_columns", 10)
dataflair4 = pd.get_option("display.max_columns")
print(dataflair4)
#10

#Pandas.reset_option
"""
With the help of the .reset_option in Pandas, you can get back the default values which may change previously.
"""

pd.reset_option("display.max_rows")
dataflair5= pd.get_option("display.max_rows")
print(dataflair5)
#60

pd.reset_option("display.max_columns")
dataflair6= pd.get_option("display.max_columns")
print(dataflair6)
#0

#Pandas.describe_option
"""
The .describe_option in Pandas describes the parameter. 
For example .describe_option(“display.max_rows”) would give the details about “display.max_rows” .
"""
print(pd.describe_option("display.max_rows"))
"""
display.max_rows : int
    If max_rows is exceeded, switch to truncate view. Depending on
    `large_repr`, objects are either centrally truncated or printed as
    a summary view. 'None' value means unlimited.

    In case python/IPython is running in a terminal and `large_repr`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the height of the terminal and print a truncated object which fits
    the screen height. The IPython notebook, IPython qtconsole, or
    IDLE do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    [default: 60] [currently: 60]
None
"""

#Pandas.option_context
"""
Using .opton_context function we can invoke a pandas option function which will be only active within the scope of the function.
In the below example, display.max_rows is set to 30 only inside the .option-context scope. 
Outside the function scope, it returns back to being 60.
"""
print("\n\n")
with pd.option_context("display.max_rows", 30):
    print(pd.get_option("display.max_rows"))  #30

print(pd.get_option("display.max_rows"))  #60


=======
import numpy as np
import pandas as pd


#Pandas.get_option()
"""
With the help of .get_option in pandas, we can define parameter which will give us a particular detail about the default values in pandas.
Using “display.max_rows” and “display.max_columns” as parameters we get a maximum number of rows and columns that can display by default.
"""
dataflair = pd.get_option("display.max_rows")
print(dataflair)
"""
60
"""

dataflair2 = pd.get_option("display.max_columns")
print(dataflair)
"""
60
"""

#Pandas.set_option()
"""
The .set_option() function allows us to change a default value to something of our choice. 
In the example given below, we see that we can change the “display.max_rows” from 60 to 90.
"""
pd.set_option("display.max_rows", 90)
dataflair3 = pd.get_option("display.max_rows")
print(dataflair3)
#90

pd.set_option("display.max_columns", 10)
dataflair4 = pd.get_option("display.max_columns")
print(dataflair4)
#10

#Pandas.reset_option
"""
With the help of the .reset_option in Pandas, you can get back the default values which may change previously.
"""

pd.reset_option("display.max_rows")
dataflair5= pd.get_option("display.max_rows")
print(dataflair5)
#60

pd.reset_option("display.max_columns")
dataflair6= pd.get_option("display.max_columns")
print(dataflair6)
#0

#Pandas.describe_option
"""
The .describe_option in Pandas describes the parameter. 
For example .describe_option(“display.max_rows”) would give the details about “display.max_rows” .
"""
print(pd.describe_option("display.max_rows"))
"""
display.max_rows : int
    If max_rows is exceeded, switch to truncate view. Depending on
    `large_repr`, objects are either centrally truncated or printed as
    a summary view. 'None' value means unlimited.

    In case python/IPython is running in a terminal and `large_repr`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the height of the terminal and print a truncated object which fits
    the screen height. The IPython notebook, IPython qtconsole, or
    IDLE do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    [default: 60] [currently: 60]
None
"""

#Pandas.option_context
"""
Using .opton_context function we can invoke a pandas option function which will be only active within the scope of the function.
In the below example, display.max_rows is set to 30 only inside the .option-context scope. 
Outside the function scope, it returns back to being 60.
"""
print("\n\n")
with pd.option_context("display.max_rows", 30):
    print(pd.get_option("display.max_rows"))  #30

print(pd.get_option("display.max_rows"))  #60


