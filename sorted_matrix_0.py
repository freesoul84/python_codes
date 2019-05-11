test=int(input())
for _ in range(test):
    m=int(input())
    length=m*m
    array=list(map(int,input().split()))
    value=sorted(array)
    count=0
    for i in range(m*m):
        if value[i]==0:
            count+=1

    print(count)
