n = int(input())

largest = -500
second_largest = -500
third_largest = -500

x = 0

while x != n:
    x += 1
    num = int(input())
    if num > largest:
        third_largest = second_largest
        second_largest = largest
        largest = num
        continue

    if num > second_largest:
        third_largest = second_largest
        second_largest = num
        continue
        
    if num > third_largest:
        third_largest = num
        continue
  
if n == 0:
    pass
else: print(f"{largest}, {second_largest} and {third_largest}")