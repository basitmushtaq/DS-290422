import string


sentence=input()
sp_ch=string.punctuation
flag=True
for ch in sp_ch:
    if ch in sentence:
        flag=False
        break

if flag:
    print('String is accepted')
else:
    print('String is not accepted')
