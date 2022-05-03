lines = int(input())

for n in range(lines):
    my_list = list(map(int, input().split(',')))

    if sorted(my_list) == my_list:
        print("true")
    else:
        print('false')
