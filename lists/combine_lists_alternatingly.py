nums_list1 = input()
list1  = nums_list1.split(',')

nums_list2 = input()
list2  = nums_list2.split(',')

list3 = []

for elem in range(len(list2)):
        list3.append(list1[elem])
        list3.append(list2[elem])
    

print(*list3, sep = ',')