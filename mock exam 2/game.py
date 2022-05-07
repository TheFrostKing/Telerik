num = abs(int(input()))
n1 = int(str(num)[0])
n2 = int(str(num)[1])
n3 = int(str(num)[2])
results = []

if num:
    results.append(n1 + n2 + n3)
    results.append(n1 + n2 * n3)
    results.append(n1 * n2 + n3)
    results.append(n1 * n2 * n3)

print(max(results))