import pandas as pd
import numpy as np
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}
df=pd.DataFrame(data)
print(df.head(2)) #retrieve from beginning 
print(df.tail(2)) # retreive from end 
print(df.iloc[1:3]) #retreive from a certain point 
print(df.loc[1:3,["Age","Salary"]]) #retreive from a certain point for certain columns
print(df[["Age","Department"]]) # to retrieve columns

 # print(df.drop("Age",axis=1,inplace=True))  to delete a column
print(df.shape)
print(df.info())
print(df.describe())

#Broadcasting
df["Salary"]=df["Salary"]+5000
print(df["Salary"])

#renaming a column
df.rename(columns={"Department":"Dept"},inplace=True)
print(df)

#to find unique values in a column
print(df["Dept"].unique())

#to find count for each unique value of a column
print(df["Dept"].value_counts())

#to create a new column based of an old one
df["Promoted Salary"]=df["Salary"]+20000
print(df)
