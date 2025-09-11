def wordchecker(s):
    wordcount=1
    for char in s:
            if char==' ':
                wordcount+=1
    return wordcount if s else 0
s=input("enter a string:")
print("The number of words in the string are:",wordchecker(s))

