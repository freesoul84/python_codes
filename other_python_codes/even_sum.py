def function(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    pri=[]
    for p in range(2,n):
        if prime[p]:
            pri.append(p)

    return pri
test=int(input())
for _ in range(test):
    num=int(input())
    if num%2==0:
        prime=function(num)
        for i in prime:
            v=num-i
            if v in prime:
                print(str(i)+" "+str(v))
                break
