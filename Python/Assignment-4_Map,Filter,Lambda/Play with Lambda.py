'''Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

sample input: 10

sample output: 35'''
func=lambda number:number+25
result=func(int(input()))
print(result)
