def function(n):
    ugly=[False for i in range(n+n)]
    p=2
    while(p<=n):
        if p==2 or p==3 or p==5:
            if(ugly[p]==False):
                ugly[p]=True
                for i in range(p,n+n,p):
                    ugly[i]=True
        if(p==5):
            break
        p+=1
    u=[1]
    for p in range(2,n+n):
        if ugly[p]:
            u.append(p)
    print(u)
    return u

test=int(input())
for _ in range(test):
    num=int(input())
    ugly=function(num)
    print(ugly[num-1])
