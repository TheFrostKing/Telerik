n = int(input())
isOdd = False
result_odd = 1
result_even = 1
x = 0
while x != n:
    x+=1
    num = int(input())
    if isOdd == False:
        result_odd = result_odd * num
        isOdd = True
        continue
    result_even = result_even * num
    isOdd =False

if result_even == result_odd:
    print(f"yes {result_even}")

else: print("no", result_odd, result_even)