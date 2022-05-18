#Python program to count the number of vowels in a given string.
sentence=input().lower()
vowels=['a','e','i','o','u']
count=0
for vowel in vowels:
    if vowel in sentence:
        count+=1
print(count)
