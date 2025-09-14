def word_frequency(s):
    s=s.lower()
    s=''.join(char for char in s if char.isalnum() or char.isspace())
    words=s.split()
    word_counts={}
    for word in words:
        word_counts[word]=word_counts.get(word,0)+1
    return word_counts
s=input("Enter a string:")
print(word_frequency(s))