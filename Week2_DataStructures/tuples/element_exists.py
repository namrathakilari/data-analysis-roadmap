def element_exists(t,num):
    if num in t:
        print("Element Found")
    else:
        print("Element not found")
t=(2,3,5,64)
num=int(input("Enter the element that is to be found:"))
element_exists(t,num)