my_list = list(map(int, input().split(',')))  

count = 1
missing = []

for x in range(len(my_list)):
    if count not in my_list:
        missing.append(count)
    count += 1
        
        
print(*missing, sep =',')

