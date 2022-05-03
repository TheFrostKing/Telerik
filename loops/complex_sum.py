import math
from decimal import Decimal
n = int(input())
x = float(input())
current_n=0
result = 0

while current_n <= n:
    result += math.factorial(current_n)/x**(current_n)
    current_n += 1

print(round(Decimal(result),5))