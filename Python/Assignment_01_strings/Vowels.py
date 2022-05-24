#Python program to count the number of vowels in a given string.
sentence=input().lower()
vowels=['a','e','i','o','u']
count=0
for alpha in sentence:
       if alpha in vowels:
        count+=1
print(count)
