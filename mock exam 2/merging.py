lines = int(input())
num_lst = []
merged_lst = []
squashed_lst = []

while lines != 0:
    num = int(input())
    num_lst.append(num)
    lines -= 1

for num in range(len(num_lst)-1):
    merged_lst.append(str(num_lst[num])[1] + str(num_lst[num+1])[0])
    n1 = int(str(num_lst[num])[1])
    n2 = int(str(num_lst[num+1])[0])
    summed = n1+n2
    if summed >= 10:
        summed = str(summed)[1]
    squashed_lst.append(str(num_lst[num])[0] + str(summed) + str(num_lst[num+1])[1])


print(*merged_lst, sep = ' ')
print(*squashed_lst, sep = ' ')