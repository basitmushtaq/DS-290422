'''Write a Python program to square the elements of a list using map() function.



Sample List: [4, 5, 2, 9]

Square the elements of the list:

[16, 25, 4, 81]

'''
try:
    input_list=list(map(int,input('enter list of numbers separated by space: ').split()))
    output_list=list(map(lambda number:number**2,input_list))
    print(output_list)
except:
    print('invalid input')

