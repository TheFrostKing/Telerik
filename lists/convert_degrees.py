my_list = list(map(int, input().split(' ')))

for n in my_list:
    converted = n  * 9/5 + 32 
    print(round(converted))
