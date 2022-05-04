n = str(input())
result = 0

for char in str(n):
    if char == '.' or char == '-':
        continue
    result += int(char)
    
n = result

while n > 9:
    result = 0
    for char in str(n):
        if char == '.' or char == '-':
            continue
        result += int(char)

    n = result

print(n)





