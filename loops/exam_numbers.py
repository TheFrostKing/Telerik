x = int(input())
y = int(input())
t = int(input())

while x <= y and x >= 100 and y <= 999:
    result = 0
    for digit in str(x):
        result += int(digit)
    if result == t:
        print(x)
    x+=1