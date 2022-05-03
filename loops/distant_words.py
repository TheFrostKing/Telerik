from decimal import Decimal

def alphabet_position(text):

    d = {L: str(i) for i, L in enumerate('abcdefghijklmnopqrstuvwxyz', 1)}

    sum = 0
    result = ''
    for t in text.lower():
        result = d.get(t, t)
        sum+=int(result)
    return sum


target = int(input())
lines  = int(input())
count_words = lines
sum_distances = 0 
words = []
while lines != 0:
    word = str(input())
    words.append(word)
    lines -= 1

for word in words:
    diff = abs(target - alphabet_position(word))
    print(f"{word} {diff}")
    sum_distances += diff   
    

print(round(Decimal(sum_distances/count_words),2))