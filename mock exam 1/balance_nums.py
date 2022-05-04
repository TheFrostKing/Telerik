result = 0

while True:
    num = abs(int(input()))

    n1 = int(str(num)[:1])

    n3 = int(str(num)[-1])

    n2 = int(str(num)[-2])

    sum_of_two_dig = n1 + n3

    if sum_of_two_dig == n2:
        result += num
        continue
    else:
        print(result)
        break

   