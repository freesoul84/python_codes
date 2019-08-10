test=int(input())
for _ in range(test):
    k,l,r,x,y=map(int,input().split())
    for b in range(x,y+1):
        a=k*b
        if a in range(l,r+1):
            print("YES")
            break
    else:
        print("NO")
