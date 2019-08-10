test=int(input())
for _ in range(test):
    num=int(input())
    u,l=map(int,input().split())
    count=0
    for i in range(u+1,l):
        n=i
        while n>0:
            r=n%10
            if r==num:
                count+=1
            n=n//10

    print(count)
