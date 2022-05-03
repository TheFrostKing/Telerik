nums_list1 = input()
my_list  = nums_list1.split(',')

new_list = []
for elem in range(len(my_list)):
     if my_list[elem] not in new_list:
        new_list.append(my_list[elem])

print(*new_list, sep = ',')