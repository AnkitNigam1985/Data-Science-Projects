import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataflair = pd.read_csv(
    "https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

print(dataflair.head())
"""
   longitude  latitude  ...  median_income  median_house_value
0    -114.31     34.19  ...         1.4936             66900.0
1    -114.47     34.40  ...         1.8200             80100.0
2    -114.56     33.69  ...         1.6509             85700.0
3    -114.57     33.64  ...         3.1917             73400.0
4    -114.57     33.57  ...         1.9250             65500.0

"""

#Plotting Histogram
dataflair["households"].hist()
plt.show()


#Plotting line chart
dataflair.plot.line(x='population', y='median_income', figsize=(8, 6))
plt.show()


#Scatter plot
dataflair.plot.scatter(x='population', y='median_income', figsize=(8, 6))
plt.show()

#Boxplot
"""
A boxplot is basically a five number summary of the data. 
It consists of the minimum, maximum, first quartile, median or second quartile, 
and the third quartile. The small dots are the outliers of the data
"""
dataflair.plot.box(figsize=(8, 6))
plt.show()


#Hexagonal Chart
"""
In such a graph a hexagon represents points of intersection. 
The increase in the points of intersection increases the darkness of the color of the hexagon
"""
dataflair.plot.hexbin(x='population', y='median_income',
                      gridsize=30, figsize=(8, 6))
plt.show()


#Pie-charts
"""
Used for categorical data segregation 
"""

dataflair1 = pd.DataFrame({'cost': [79, 40, 60]}, index=[
                         'Oranges', 'Bananas', 'Apples'])
dataflair1.plot.pie(y='cost', figsize=(8, 6))
plt.show()

#Kernal density plot
dataflair["median_income"].plot.kde(color='r')
plt.show()