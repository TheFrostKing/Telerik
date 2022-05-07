#The digit zero (0) is considered to be even.
num = input()
result_even = 0
result_odd = 0

for digit in num:
    if int(digit) % 2 == 0:
        result_even += int(digit)
    else:
        result_odd += int(digit)

if result_odd > result_even:
    print(f"{result_odd} cups of coffee")

elif result_odd < result_even:
    print(f"{result_even} energy drinks")

else:
    print(f"{result_even} of both")