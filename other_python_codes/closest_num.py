test=int(input())
for _ in range(test):
    n,m=map(int,input().split())
    if n>=0 and n>=m:
        v=n//m
        print(v*m)
    elif n<0:
        v=n//m
        v1=v+1
        if abs(n-(v1*m))<abs(n-(v*m)):
            print(v1*m)
        else:
            print(v*m)

    
