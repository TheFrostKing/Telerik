nums_list = input()
my_list  = nums_list.split(',')
times_to_rotate = int(input())

while times_to_rotate != 0:

    first = my_list.pop(0)
    my_list.append(first)

    times_to_rotate -= 1

print(*my_list, sep = ',')