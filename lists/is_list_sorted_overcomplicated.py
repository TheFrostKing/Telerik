num_of_lines = int(input())


for n in range(num_of_lines):
    isSorted = 'true'
    my_list = list(map(int, input().split(',')))

    for num in range(len(my_list)-1): 
        if my_list[num] > my_list[num+1]:
            isSorted = 'false'
            break
        
    print(isSorted)