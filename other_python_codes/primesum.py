def function(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    pri=[]
    for p in range(2,n+1):
        if prime[p]:
            pri.append(p)

    return sum(pri)
test=int(input())
for _ in range(test):
    num=int(input())
    print(function(num))
