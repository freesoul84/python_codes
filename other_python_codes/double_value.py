test=int(input())
for _ in range(test):
    n,b=map(int,input().split())
    array=sorted(list(map(int,input().split())))
    for i in range(n):
        if b in array:
            b=b*b
        else:
            print(b)
            break
