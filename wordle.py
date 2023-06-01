#Todo
#Make letter frequencies for 5 letter words
#get suggestions for the best word to try now when theres a lake of info
#make it all user friendly through adding new info to lists and/or dictionaries

file1 = open('wordle.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    flag = True
    word=line.strip()
    if 'a' in word and word[4]=='e' and 'u' in word:
        for i in range (0, 5):
            if word[i] in ('i', 'r', 't', 'v', 'g'):
                flag=False
        if word[2]=='a':
            flag=False
        if flag==True:
            print(word)
