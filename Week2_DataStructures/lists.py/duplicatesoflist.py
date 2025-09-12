def duplicatesOfList(l):
    l.sort()
    duplicates=[]
    for i in range(len(l)-1):
        if l[i]==l[i+1] and l[i] not in duplicates:
            duplicates+=l[i]
    return duplicates     
size=int(input("enter the size of the list:"))
print("Enter the elements of the list:")
l=[]
for i in range(size):
    num=input()
    l.append(num)
print("The duplicates of the list are:",duplicatesOfList(l))