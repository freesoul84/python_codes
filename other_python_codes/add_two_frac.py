test=int(input())
for _ in range(test):
    d1,d2,n1,n2=map(int,input().split())
    if d1==d2:
        val=(n1+n2)/d1
        print(val)
    else:
        val=(n1*d2+n2*d1)/(d1+d2)
    print(val)
