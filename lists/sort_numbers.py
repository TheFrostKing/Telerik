nums = str(input())

make_list = [int(i) for i in nums.split(', ')]
make_list.sort(reverse=True)
print(*make_list, sep=', ')