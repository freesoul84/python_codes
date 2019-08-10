#geks cold coffee
test=int(input())
for i in range(test):
    n,m=map(int,input().split())
    count=1
    while n>0:
        if count==m:
            print(n)
            break
        n=n//2
        count+=1
