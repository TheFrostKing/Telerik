input_lst =list(map(int,input().split(', ')))
target = int(input())

for digit in range(len(input_lst)):
    if digit == 0 or digit == len(input_lst)-1:
        continue
    
    if input_lst[digit-1] != input_lst[digit] and  input_lst[digit] != input_lst[digit+1] and target == input_lst[digit]:
        if input_lst[digit+1] > input_lst[digit-1]:
            input_lst[digit] = input_lst[digit+1]
        else:
            input_lst[digit] = input_lst[digit-1]

print(input_lst)
            