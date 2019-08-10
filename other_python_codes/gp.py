test=int(input())
for _ in range(test):
    n=int(input())
    a,r=map(int,input().split())
    if((r-1)!=0):
        value=a*(r**n-1)/(r-1)
        print("{0:.6f}".format(value))
    else:
        print("{0:.6f}".format(a*n))
