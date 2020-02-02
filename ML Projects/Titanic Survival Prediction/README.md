# EDA on Titanic Dataset

This is the analysis on the Titanic dataset containing data of passengers travelled in Titanic

[![](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic1.png)](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic1.png)

Example missing value for Age is replaced by the median age in the dataset.

And if missing value in Embarked columnI(i.e boarding station), it is replaced by most common values for Embarked column.

Checked the relationship between input features and target variable using heatmap

Checked the distribution of target variable using Seaborn KDE plot.

Some major analysis made on the data set

**1. Missing values are analyzed and replaced them with the appropriate values**

[![Missing values](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic2.png "Total missing values")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic2.png "Total missing values")


**Categorical replaced by mode(most common) values****

[![Handling categorical missing values](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic8.PNG "Handling categorical missing values")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic8.PNG "Handling categorical missing values")


**Numerical replaced by median values**

[![Handling numerical missing values](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/Titanic7.PNG "Handling numerical missing values")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/Titanic7.PNG "Handling numerical missing values")


**2. Dropping the columns not needed for analysis**

[![Dropping the columns](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic10.PNG "Dropping the columns")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic10.PNG "Dropping the columns")


**3. Relationship  between features studied using pair plot**

[![Relationship between input features](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic13.PNG "Relationship between input features")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic13.png "Relationship between input features")

The number of people died are more than those survived.

Also, female survived more as compared to male.

High class(class-1) passengeers survived more than other classes


**4. Heatmap to study the relation between input features and target**

[![Input features and target variable](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic4.png "Input features and target variable")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic4.png "Input features and target variable")

Male gender is -ve correlated with target variable  - "Survived" while female gender is +ve correlated.

Similarly class is -ve correlated as highest class is 1 and lowest class is 3, and passengers from class 1 survived most.


**5. Distribution of target variable**

[![Survived output distribution](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic14.PNG "Survived output distribution")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic14.PNG "Survived output distribution")


**6. Different Models compared on various parameters to select best model for Prediction**

[![Survived output distribution](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic15.PNG "Survived output distribution")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic15.PNG "Survived output distribution")


[![Survived output distribution](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic16.PNG "Survived output distribution")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic16.PNG "Survived output distribution")


**7. Finalizing the Logistic model based on above observation and applying to predict the output**

[![Survived output distribution](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic17.PNG "Survived output distribution")](https://raw.githubusercontent.com/AnkitNigam1985/Data-Science/master/tmp_images/titanic17.PNG "Survived output distribution")


For detailed information, can check the presentation above and for the analysis, please refer the notebook.
