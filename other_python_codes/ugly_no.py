def ugly_no(n):
    ugly=[False for i in range(10001)]
    p=2
    while p*p<=10001:
        if p==2 or p==3 or p==5:
            if ugly[p]==False:
                ugly[p]=True
                for i in range(p*p,10001,p):
                    ugly[i]=True
        if p>6:
            break
        p+=1

    ugly_no=[1]
    for i in range(2,10001):
        if ugly[i]:
            ugly_no.append(i)
    return ugly_no

test=int(input())
for _ in range(test):
    num=int(input())
    value=ugly_no(num)
    print(value[num-1])
