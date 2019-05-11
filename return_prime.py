def sieve(n):
    prime=[True for i in range(n+1)]
    p=2
    while p*p<=n:
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    prime_no=[]
    for i in range(2,n+1):
        if prime[i]:
            prime_no.append(i)
    return prime_no

test=int(input())
for _ in range(test):
    num=int(input())
    value=sieve(num)
    for i in value:
        diff=num-i
        if diff in value:
            print(str(i)+" "+str(diff))
            break
