num = int(input())
primes = 0
primes_lst =[]
def give_prime(n):
    if n == 1:
        return True
    if n > 0 :
        for i in range(2,n):
            if n % i == 0:
                return False
        else:
            return True

for n in range(1,int(num)+1):
    if give_prime(n):
        primes += 1
        primes_lst.append(n)

# [1 2 3 5 7]

for x in range(primes):
    for prime in range(1,primes_lst[x]+1):
        if  give_prime(prime):
            print(1, end = '')
        else:
            print(0, end='')
    print(end='\n')
 

       
# # input 
# input1 = input() 

# primes=[]
# toprint=''
# for n in range(1,int(input1)+1):
#     isprime=True
#     for prime in primes:
#         if prime!=1 and n%prime==0:
#             isprime = False
#     if isprime:
#         primes.append(n)
#         toprint+="1"
#         print(toprint) 
#     else:
#         toprint+='0'