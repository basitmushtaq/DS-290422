in_word=input('Enter your Word: ')
end=len(in_word)-1
reversed_word=''
for i in range(end+1):
    reversed_word+=(in_word[end-i])
print(reversed_word)