test=int(input())
for _ in range(test):
    a,b=map(int,input().split())
    a,b=b,a
    print(str(a)+" "+str(b))
