#Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of non-empty tuples

N=int(input("enter the number of tuples in list: "))
tup_list=[]
for i in range(N):
    input1=input('enter elements of tuple separated by \',\': ')
    tuple1=tuple(map(int,input1.split(',')))
    tup_list.append(tuple1)
#sort
for i in range(len(tup_list)-1):
    for j in range(1,len(tup_list)):
        if tup_list[i][-1]>tup_list[j][-1]:
            tup_list[i],tup_list[j]=tup_list[j],tup_list[i]
print(tup_list)

