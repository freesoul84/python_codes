test=int(input())
for _ in range(test):
    n,d=map(int,input().split())
    car=list(map(int,input().split()))
    price=list(map(int,input().split()))
    v=[]
    if d%2==0:
        for i in range(len(car)):
            if car[i]%2==1:
                v.append(i)
    else:
        for i in range(len(car)):
            if car[i]%2==0:
                v.append(i)
    print(sum([price[i] for i in v]))
