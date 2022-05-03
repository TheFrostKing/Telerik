my_list = list(map(int,input().split(',')))

zeroes = []

for elem in range(len(my_list)): 
    if my_list[elem] == 0:
        zeroes.append(my_list[elem])

my_list = [i for i in my_list if i != 0]

result = my_list+zeroes
print(*result, sep=',')