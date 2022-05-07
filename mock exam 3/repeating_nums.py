import random
from collections import Counter

lines = int(input())
num_lst = []


while lines != 0:
    num_lst.append(int(input()))
    lines -= 1

most_common,num_most_common = Counter(sorted(num_lst)).most_common(1)[0]


print(most_common)
