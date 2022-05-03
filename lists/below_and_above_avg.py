from decimal import Decimal


def Average(lst):
    return sum(lst) / len(lst)

my_list = list(map(int, input().split(',')))
below = []
above = []

list_avg = Average(my_list)

for elem in my_list:
    if elem > list_avg:
        above.append(elem)
    if elem < list_avg:
        below.append(elem)

print(f"avg: {round(Decimal(list_avg),2)}")

print("below:", end='')
print(*below, sep =',')

print("above:",end = ' ')
print(*above, sep=',')




