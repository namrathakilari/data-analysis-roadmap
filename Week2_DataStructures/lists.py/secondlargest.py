def secondLargest(l):
    largest=max(l)
    l2=l.copy()
    l2.remove(largest)
    secondl=max(l2)
    return secondl
size=int(input("enter the size of the list:"))
print("Enter the elements of the list:")
l=[]
for i in range(size):
    num=input()
    l.append(num)
print("the second largest element is:",secondLargest(l))


