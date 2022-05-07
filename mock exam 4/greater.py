arr1 = list(map(int, input().split(',')))
arr2= list(map(int, input().split(',')))
count = 0
toStart = False
result = []

for num in arr1:
    if count == 0 and toStart:
        result.append(-1)
    toStart = False
    count = 0
    for n in range(0,len(arr2)-1):
        if num == arr2[n]:
            toStart = True
        if num < arr2[n+1] and toStart:
            result.append(arr2[n+1])
            count+=1
            break
        if num >= arr2[n+1] and toStart:
            continue
        if num == arr2[len(arr2)-1]:
            result.append(-1)
            break

            
print(*result, sep=',')    
 

    

