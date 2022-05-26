#Write a Python function to sum all the numbers in a list.
def sum_list(lis):
    sum=0
    for item in lis:
        sum+=item
    return sum

lis=list(map(int,input("enter space separated elements of list: ").split()))
sum_of_list=sum_list(lis)
print(sum_of_list)