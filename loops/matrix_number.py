n = int(input())
rows = n
for a in range(1,n+1):
    rows+=1
    for c in range(a,rows):
        print(c, end=" ")
    print("\n")