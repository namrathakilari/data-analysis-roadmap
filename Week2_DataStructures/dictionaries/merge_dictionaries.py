d={}
n=int(input("enter the size of the dictionary1:"))
for i in range(n):
    key=input("Enter key:")
    value=input("Enter value:")
    d[key]=value
d1={}
m=int(input("enter the size of the dictionary2:"))
for i in range(m):
    key=input("Enter key:")
    value=input("Enter value:")
    d1[key]=value
merged_dict=d|d1
print(merged_dict)