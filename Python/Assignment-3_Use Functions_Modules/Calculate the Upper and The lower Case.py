# Write a Python function that accepts a string and 
#calculate the number of upper case letters and lower case letters.

def count_lower_upper(string):
    upper=0
    lower=0
    for item in string:
        if item.islower():
            lower+=1
        elif item.isupper():
            upper+=1
    return lower,upper

string=input("enter string: ")
lower,upper=count_lower_upper(string)
print("No. of Upper case characters : ",upper,"\nNo. of Lower case Characters : ",lower)

