def CheckElement(title, word):
    fake = title_lst
    result = []

    for char in word:
        for ch in range(len(title)):
            
            if char == title[ch]:

                result.append(title[ch])
                fake.pop(ch)
                break      

    if result == word:
        wrd = ''.join(fake)
        return wrd
    else:
        return 'No such title found!'
                
    

title = input().lower()
result = []
words = []
title_lst=[]

for ch in title:
    title_lst.append(ch)

lines = int(input())

while lines != 0:
    
    words.append(input())
    lines -= 1

for word in words:
    word_lst =[]
    for ch in word:
        word_lst.append(ch)

    result.append(CheckElement(title_lst, word_lst))
 
print(*result, sep = '\n')

                

        


