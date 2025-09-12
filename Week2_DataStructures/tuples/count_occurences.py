def count_occurences(t,val):
    count=0
    for i in range(len(t)):
        if t[i]==val:
            count+=1
    return count
t=(1,2,1,3,1,4)
val=int(input("Enter the value for which occurences are to be found:"))
print("Count:",count_occurences(t,val))