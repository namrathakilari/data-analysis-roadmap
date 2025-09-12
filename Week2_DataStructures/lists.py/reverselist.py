def reverse(l):
    l.reverse()
    return l
size=int(input("enter the size of the list:"))
print("Enter the elements of the list:")
l=[]
for i in range(size):
    num=input()
    l.append(num)
print("The reversed list is:")
print(reverse(l))