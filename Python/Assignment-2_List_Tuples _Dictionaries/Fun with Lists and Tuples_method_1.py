#Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of non-empty tuples

N=int(input("enter the number of tuples in list: "))
tup_list=[]
for i in range(N):
    input1=input('enter elements of tuple separated by \',\': ')
    tuple1=tuple(map(int,input1.split(',')))
    tup_list.append(tuple1)
tup_list.sort(key=lambda tup: tup[-1])
print(tup_list)