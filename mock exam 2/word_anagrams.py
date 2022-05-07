word_to_find = str(input())
lines = int(input())
prints = []
while lines != 0:
    word = str(input())
    word_lst = []
    word_lst.append(word)
    make_char = []
    result = []
    for char in word_to_find:
        make_char.append(char)
    for char in word:
        result.append(char)

    if sorted(result) == sorted(make_char):
        prints.append('Yes')
    else:
         prints.append('No')

    lines -= 1

print(*prints, sep = '\n')