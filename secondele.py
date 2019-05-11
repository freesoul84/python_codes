test=int(input())
for _ in range(test):
    num=int(input())
    array=sorted(set(list(map(int,input().split()))))

    if len(array)>=2:
        print(array[-2])
    else:
        print(-1)
