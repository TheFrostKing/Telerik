my_list = list(map(int, input().split(',')))

x= 0

positive = []
positives_before_zero = []
zeroes = []
negative = []

for elem in my_list:
    if elem == 0:
        zeroes.append(elem)
    
    elif elem < 0: 
        negative.append(elem)   

    elif elem > 0:
        positive.append(elem)


final_list = negative + zeroes + positive

print(*final_list, sep=',')
