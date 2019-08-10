test=int(input())
for _ in range(test):
    m,n=map(int,input().split())
    if m!=n:
        val= m ^ n
        for i in range(0,len(str(bin(val)))-2,1):
            val2=val>>i & 1
            if val2==1:
                print(i+1)
                break
    else:
        print(-1)
