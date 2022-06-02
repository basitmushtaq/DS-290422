'''Write a Python program to triple all numbers of a given list of integers. Use Python map.

sample list: [1, 2, 3, 4, 5, 6, 7]
Triple of list numbers:
[3, 6, 9, 12, 15, 18, 21]
'''
try:
    input_list=list(map(int,input('enter list of numbers separated by space: ').split()))
    output_list=list(map(lambda number:number*3,input_list))
    print(output_list)
except:
    print('invalid input')

