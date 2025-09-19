import pandas as pd
import numpy as np
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}
df=pd.DataFrame(data)
df.rename(columns={"Department":"Dept"},inplace=True)
df["Promoted Salary"]=df["Salary"]+20000

#data cleaning 
 #   df.dropna(how="any") if any value of a row is null
 #   df.dropna(how="all") if all values of a row is null 
print(df["Age"].fillna(df["Age"].mean()))
print(df["Salary"].fillna(df["Salary"].median()))
print(df["Age"].fillna(method="ffill"))
print(df["Age"].fillna(method="bfill"))

print(df["Name"].replace("Bob","Rose"))

#duplicates
df_dup=df[df.duplicated()]

df=df.drop_duplicates()

#method and lambda
df["Promoted Salary"]=df["Promoted Salary"].apply(lambda x:x/10 if x>65000 else x)
# name= "alice_fernandez"
# df[[first_name","last_name"]]=df["Name"].str.split("_")



