test=int(input())
for _ in range(test):
    num=int(input())
    array=list(map(int,input().split()))
    for i in range(len(array)-1):
        if array[i]<array[i+1]:
            continue
        else:
            print(0)
            break
    else:
        print(1)
