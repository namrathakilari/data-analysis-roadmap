d={}
n=int(input("enter the size of the dictionary:"))
for i in range(n):
    key=input("Enter key:")
    value=input("Enter value:")
    d[key]=value
print("The maximum value's key is: ")
max_value=max(d.values())
for key,value in d.items():
    if value==max_value:
        print(key)

        