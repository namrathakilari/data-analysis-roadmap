def subset_check(s1,s2):
    for element in s2:
        if element not in s1:
            return False
        return True
s1={1,2,3,4}
s2={2,4}
print(subset_check(s1,s2))

