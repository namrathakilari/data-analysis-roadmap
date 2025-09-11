def calculator(n1,n2,c):
    match c:
        case "+":
            result=n1+n2
            return result
        case "-":
            result=n1-n2
            return result
        case "*":
            result=n1*n2
            return result
        case "/":
            try:
                result=n1/n2
                return result
            except ZeroDivisionError:
                print("ERROR: cannot divide by zero!")
           
n1=float(input("Enter number 1: "))
n2=float(input("Enter number 2: "))
c=(input("Enter the operation(+,-,* or /):"))
print("Result:",calculator(n1,n2,c))