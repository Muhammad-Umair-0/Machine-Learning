import pandas as pd 
import numpy as np
df = pd.DataFrame()
print(df)

# from list to dataframe 
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
df = pd.DataFrame(lst)
print(df)

# Creating Dataframe from Dict of numpy
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=["A", 'B','C'])
print(df)


# Creating dataFrame from List of Dictionaries 
print("from Dictionary")
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

df = pd.DataFrame(dict)
print(df)

#  pandas Indexing 
data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 48000]}
df = pd.DataFrame(data)
print(df)
print(df.index, "\n\n")

# Setting a custom index
print("With set index")
df_custom_idx = df.set_index(['Name'], drop= True, inplace=False)
print(df_custom_idx)

# reset index
print("with reset index")
reset_idx = df_custom_idx.reset_index()
print(reset_idx)


# indexing  with loc

print("Indexing with loc")
try:
        row = df_custom_idx.loc['Bob']
        print(row)
except KeyError:
        print("Name 'Bob' not found in index")

# Pandas Access DataFrame
print("Accessing DataFrames \n\n")

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(df)
print(df)

#accessing Columns from dataFrame
print("Accessing Columns")
age_col = df['Age']
print(age_col)

# accessing row by index
sec_row = df.iloc[1]
print("The Row")
print(sec_row)

# accessing multiple row or columns 
print("Accessing multiple Row or columns")
subset = df.loc[0:2,['Name','Age']]
print(subset)

# Filtering DataFrame based on condition
print("Filtering DataFrame based on condition")
filter_data = df[df['Age']>25]
print(filter_data)

#  to access specific Cell 
salary_index_2 = df.at[2, 'Salary']
print(salary_index_2)

#access with ith
age_index_3 = df.iat[3, 1]
print(age_index_3)


# Indexing and Selecting Data with Pandas
print("Data set \n\n")
df = pd.read_csv('./Pandas/nba.csv')
print(df.head(5))

# select single column from dataset 
print("Selecting single column")
first = df['Age']
print(first.head(5))

# select multiple columns
print("Selecting multiple columns")
multiple = df[['Name', 'Team', 'Age']]
print(multiple.head(5))

df = df.set_index('Name')
row = df.loc['Avery Bradley']
print(row)

print(df.head())

row = df.loc[['Avery Bradley','John Holland']]
print(row)

print(df.shape)

