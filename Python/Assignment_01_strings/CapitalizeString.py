#Python program to capitalize the first and last character of each word in a string (input string should be a statement)

words=input().split()
for word in words:
    if len(word)>1:
        print(word[0].upper()+word[1:-1]+word[-1].upper(),end=' ')
    else:
        print(word.upper(),end=' ')