#Write a Python program to reverse a string.

def reverse_string(string):
    rev_string=''
    for i in range(len(string)-1,-1,-1):
        rev_string+=string[i]
    return rev_string

string=input('enter string: ')
rev_string=reverse_string(string)
print(rev_string)
