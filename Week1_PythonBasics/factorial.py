def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
num=int(input("enter a number:"))
print("the factorial is:",fact(num))