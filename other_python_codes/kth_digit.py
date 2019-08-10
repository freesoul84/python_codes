test=int(input())
for _ in range(test):
    a,b,k=map(int,input().split())
    value=a**b
    count=1
    while value>0:
        r=value%10
        if count==k:
            print(r)
            break
        value=value//10
        count+=1
