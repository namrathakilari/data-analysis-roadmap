import pandas as pd 
s=pd.Series([10,20,30,40])
s.name='calories'
print(s)
print(s.dtype)
print(s.values)
# to get rangeindex
print(s.index)
#to get name of series
print(s.name)
#indexing
print(s[0:2])
#iloc->location based indexin 
print(s.iloc[3])
print(s.iloc[[1,2,3]])

index=['apple','banana','orange','kiwi']
s.index=index
print(s)
print(s['banana'])
#loc->label based indexing 
print(s.loc['kiwi'])
print(s.loc['banana':'kiwi'])