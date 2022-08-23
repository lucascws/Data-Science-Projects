# Project 2 - Ames Housing Data and Kaggle Challenge

## Executive Summary

We are tasked with helping a property agency in predicting the prices of future house 
listings. In addition, they also need to find out what are the key information to 
collect for future house listings. Our original given dataset contains 80 variables 
describing the characteristics of the houses. In our initial findings, we found that 
the features, neighbourhood, the size of certain areas of the house, house age and 
overall quality seem to exhibit a strong relationship with Sale Prices. During our data 
processing and feature engineering, we dropped variables that are similar to one another 
or combine them into new features to avoid a multicollinearity issue. We used a 
regression model to help predict our house prices as Sale Price is a continuous 
variable. A Ridge model gave us the best R-Squared and RMSE score, suggesting that it 
is the best model. From our model, tThe most important variables in the model are above 
ground living area and overall score (Quality and Condition). The Lot Area, basement 
finishing area (Basement SF with finishing), neighbourhood and house age are also 
important features in determining Sale Price. 

## Problem Statement

Our Client is a Property Agents. They are looking to expand into the Iowa property market. We are tasked to
predict the prices of houses based on their characteristics. Our client is also interested in understanding
what are the important variables that affects house prices to identify the key characteristics.

## Key Questions
Our preliminary research suggest that some features are critical in determining house
prices. We will analyse some of this variables in particular. 
[**source**](https://www.opendoor.com/w/blog/factors-that-influence-home-value)
Some key questions are:
- Do Neighbourhood matter?
- Do house size matter?
- Is a certain area of the house more important?
- How important is the finishing of the houses?
- Does the age of the house matter?

## Data Summary

We have two datasets on the houses in Ames. The dataset describes some characteristics of the houses. In one of the dataset, we have information on the actual sale prices of the houses. Our dataset contains 80 variables that might be useful in predicting Sale prices. Our objective is to predict the prices of houses in Ames based on their characteristics that has been given in the dataset.

[**Data Dictionary**](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)


## Data Cleaning

In our dataset, there are no duplicated rows. Many of the Null values occur on the same rows for multiple columns suggesting that they are not mutually exclusive. For
instance, a few columns relating to the basement characteristics has missing values in the same rows. Comparing the unique values in each column to the data dictionary,
it seems that many of the null values are not actually missing values. Instead, it is a category itself where the feature does not exist. (such as no basement)
Apart from the Electrical column, the rest of the columns with null values appear in both train and test dataset.

For most variables with only 1 or 2 missing values, we will use the mean for numerical columns and mode for categorical columns to fill the 
null values. This will have minimal impact on the distribution of the variables. However, for some variables, such as Masonry Veneer and basement,
we managed to fill some of the missing values with one of the category which is the best fit. For instance, "None" category is used for Masonry Veneer type
and the corresponding Masonry Veneer Area value is 0, where we treat the null values as houses with no masonry veneer.
In the test dataset there is 1 missing value for the electrical column, we filled it with the most frequent value.

Some variables, such as Lot Frontage has too many missing values to be useful. We drop these columns.

## EDA

There are 42 categorical variables and 37 numerical variable (Inclusive of the Response Variable Sales Price). 

There are 21 categorical variables with not much variance as more than 80% of the data has the same value.

Some Numerical columns are correlated with one another. Overall Quality is correlated with many other variables. Other variables that are correlated are
Year Built and Year remodeled, Garage cars and Garage area. Some of these variables would have to be dropped to avoid multicollinearity. One interesting 
finding is that many of the variables relating to SF are highly correlated with one another (as well as the number of rooms). We could possibly combine
some of these features into a new consolidated Square Feet feature.

The average Sale price of houses are around \\$181,470 and 50\% of the houses cost between \\$130,000 and \\$214,000. Sale Prices has a right skewed distribution, suggesting
that some houses are much more expensive than the rest. The top 3 houses cost around \\$600,000.

Some Categorical variables that are similar can be combined to better suit the model. For instance, the quality and condition columns for several features
are very similar in terms of distribution. Creating an interaction variable between them might be useful. Another instance is combining the quality and 
count of some of the features.

Some of the numerical columns with the highest correlation to Sales Price are Overall Quality, Above Ground Living Area, Garage Area, Total Basement Square Feet 
and year Built. These variables could be the important variables to include in our model.

Most of the ordinal categorical variables seem to indicate a relationship with Sale Price in the order of their ranking. 
For two variables: Lot Shape and fence - they do not vary much in relation to Sale Price across the category.

The Nominal categorical variables seem to vary across the categories in relation to Sales Price. This is especially so in Neighbourhood and Subclass.
Perhaps these two variables would be good predictors of house prices.


## Feature Engineering

Variables that have little variation, as identified from EDA, are dropped and are not used to create new features are dropped first. We also dropped the
variables that are just unique identifier or are too similar to another column.

Ordinal Encoding is performed to categorical variables that are ordinal in nature. The ranking of the categories are referenced from the data
dictionary. Some of these variables include Exterior and Basement Quality and Condition. 

For the nominal categorical variables, One Hot Encoding is performed. 

The other feature engineering performed is the creation of new features from some of the variables. Some of these new features are interaction
between variables that are similar, such as the Quality and Condition variables for Overall, Basement and Exterior. Another feature created is the 
consolidated square feet of a certain area of the house such as the Basement, Above Ground Living area and Outdoor area. We also created a score variable
for different areas of the house such as the Bathroom, Kitchen and Fireplace using the quality and quantity of each feature. A house age variable is also
created from the Year variables.

The newly created features does seem to exhibit a relationship with Sale Price. They should be useful explanatory variables for Sale Price. Most of them 
show a positive relationship with Sale Price. The house age shows a negative relationship with Sale Price. One interesting observation is that there 
are 2 datapoints showing houses with very large square feet areas but with a relatively low sale price. We will remove this two data points.


## Model Evaluation and Selection

We will be using regression models since Sale Price is a continuous variable. The models that we will evaluate are the Linear Regression, Ridge and Lasso models. We will utilise a RMSE and R-squared metric score to identify the best regression model between the three.

|Model|CV R-Squared|Validation R-Squred|RMSE|Alpha|
|---|---|---|---|---|
|Linear Reg|0.89|0.91|23022|NA
|Ridge|0.91|0.91|22887|1.12
|Lasso|0.91|0.91|22961|1.0

The best model is Ridge
RMSE on test dataset is 21648 - Ridge Model

## Conclusion

A Regression model (Ridge) is useful in predicting Sale Prices and can be used to predict new house prices as it has a RMSE of 21648 on the test dataset (similating new data). 

The most important variable in the model are above ground living area and overall score (Quality and Condition). The Lot Area, basement finishing area (Basement SF with finishing), neighbourhood and house age are also important features in determining Sale Price.

Relating to to our problem statements and the key questions we wanted to answer.
1. Neighbourhood is a strong influencer on Sale Price - possibly because 
2. House Size is in fact the most important feature from our model
3. The inner house area above the ground floor seems to be the most valuable area
4. The overall finishing (Quality and Condition) also influences Sale Price quite significantly
5. House age is also a good predictor of houses

Limitations of our findings

There are other social, economic and political factors that are likely to heaviliy influence house prices. We are not able to control for these variables with the information provided in our dataset. Some of these factors are:
[**source**](https://www.investopedia.com/articles/mortages-real-estate/11/factors-affecting-real-estate-market.asp)
- Demographics
- Interest rate
- The Economy
- Government Policies

## Recommendation

1. We can build a Ridge Regression model to help predict prices of houses that will be added to the listing from the property agency
2. The most important data to collect are above ground living area and overall finishing (Quality and Condition), Lot Area, Basement SF & Finishing, neighbourhood and house age.
3. More external data, such as Demographics and Interest rate should be collected and added to our prediction model