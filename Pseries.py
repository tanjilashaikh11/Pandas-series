import numpy as np
import pandas as pd

# 1. Creating a Series
data=[1,2,3,4,5]
series=pd.Series(data)
print(series)

# 2. Custom Index for a Series
# a.change the default index
series=pd.Series(data,index=['a','b','c','d','e'])
print(series)
# b.change by reindexing
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
reindexed_series = series.reindex(['a', 'b', 'd'])
print(reindexed_series)
# c.Index Uniqueness
# You can check if the Series index is unique using .is_unique.
series = pd.Series([1, 2, 3], index=['a', 'b', 'a'])
print(series.index.is_unique)  # Output: False (because index 'a' is repeated)
# d. Resetting the Index
# You can reset the index of a Series using .reset_index(). This is useful when the index is not needed or needs to be set back to default.
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
reset_series = series.reset_index(drop=True)
print(reset_series)


# 3. Series from a Dictionary
dict={'x':1,'y':2,'z':3}
series=pd.Series(dict)
print(series)

# 4. Series from NumPy Array
arr=np.array([10,20,30])
series=pd.Series(arr)
print(series)

# 5. Accessing Series Elements
#    a.By index label:
#print(series['x'])
#    b.By Position
print(series[1])
#   c. Slice Data
print(series[:2])

# 6. Vectorized Operations on Series
# a. Arithmetic Operations
series1=pd.Series([1,2,3])
series2=pd.Series([4,5,6])
print(series1+series2)
print(series1+1)
#b.Element wise Comparison
print(series2>4)
#c. Math Functions
print(series1.sum())
print(series1.mean())
print(series1.std())

#7. Handling Missing Data
# a. Detecting Missing Values
series = pd.Series([1, 2, None, 4])
print(series.isnull())
# b. Filling Missing Data
print(series.fillna(0))
# c. Dropping Missing Data
print(series.dropna())

# 8.Series Alignment
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([4,5,6],index=['a','b','d'])
print(s1+s2)
'''Output: 
a    5.0
b    7.0
c    NaN
d    NaN
dtype: float64'''

# 9.Applying Functions to a Series
def square(x):
    return x*x

series=pd.Series([1,2,3,4])
squared_series=series.apply(square)
print(squared_series)

# b. Lambda Functions
cubed_series=series.apply(lambda x: x*x*x)
print(cubed_series)

#10. Data Type handling
print(series.dtype)

#change the datatype
print(series.astype(float))  # Converts to float64

#11.
# a.Assigning a Name to a Series useful in Large Datasets for identification

series = pd.Series([1, 2, 3], name="MySeries")
print(series)

# b. Assigning a Name to the Index
series.index.name = "IndexName"
print(series)

# 12. Converting Series to Other Data Structures
# a. Series to List
list_data = series.tolist()
print(list_data)  # Output: [1, 2, 3]

dict_data = series.to_dict()
print(dict_data)  # Output: {0: 1, 1: 2, 2: 3}

# 13. String Operations in a Series
# a. Basic String Manipulation
series = pd.Series(['apple', 'banana', 'cherry'])
print(series.str.upper())  # Converts all to uppercase

# b. Finding Substrings
print(series.str.contains('an'))  # Checks if 'an' is in each string

# # 13. Sorting a Series
# a. Sort by Values
# You can sort a Series by its values using .sort_values().
series = pd.Series([3, 1, 2], index=['a', 'b', 'c'])
print(series.sort_values())
# b. Sort by Index
# You can sort a Series by its index using .sort_index().
print(series.sort_index)

# #15.Handling Duplicates in Series
# a. Check for Duplicates
# You can use .duplicated() to identify duplicate values.
print(series.duplicated())
# b. Remove Duplicates
# You can remove duplicates using .drop_duplicates().
print(series.drop_duplicates())

# 16. Working with Date-Time in Series
# a. Creating a Series with Datetime
dates = pd.date_range('20230101', periods=6)
series = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
print(series)
#b.Date Time Manipuation
print(series.index.year)   # Extracts the year
print(series.index.month)  # Extracts the month


# #17.Combining Series
# a. Appending Series
# You can append one Series to another using .append().
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])
combined = series1.append(series2)
# print(combined)
# b. Concatenating Multiple Series
# Pandas provides the .concat() method to concatenate multiple Series.
combined = pd.concat([series1, series2])
print(combined)

