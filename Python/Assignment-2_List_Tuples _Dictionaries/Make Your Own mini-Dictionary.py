#Write a Python program to print a dictionary whose keys should be the
#  alphabet from a-z and the value should be corresponding ASCII values
mini_dict=dict()
for i in range(ord('a'),ord('z')+1):
    mini_dict[chr(i)]=i
print(mini_dict)