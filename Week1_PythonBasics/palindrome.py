def palindrome(s):
    for i in range(0,len(s)):
        if(s[i]!=s[len(s)-i-1]):
            return False
        return True 
    
s=input("enter the string:")
if(palindrome(s)):
    print("It is a Palindrome")
else:
    print("It is not a palindrome")