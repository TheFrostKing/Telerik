n = int(input())
max_num = -200
x = 0

while x != n:
    num = int(input())
    if num > max_num:
        max_num = num 
    x += 1
if n == 0:
    pass
else: print(max_num)