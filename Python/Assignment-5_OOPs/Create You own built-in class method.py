"""Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
You must implement it using Class
Sample Input:
x: 10
n: 2
Sample Output:
100
"""
from Class import *
base=int(input("X: "))
exp=int(input('n: '))
power_obj=power(base,exp)
result=power_obj.execute()
print(result)