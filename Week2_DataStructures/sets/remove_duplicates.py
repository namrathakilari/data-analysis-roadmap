def remove_duplicates(l):
    set1=set(l)
    l1=list(set1)
    return l1
size=int(input("enter the size of the list:"))
print("Enter the elements of the list:")
l=[]
for i in range(size):
    num=input()
    l.append(num)
print("After removing duplicates:",remove_duplicates(l))