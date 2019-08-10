test=int(input())
for _ in range(test):
    n,m=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    for i in arr1:
        if i not in arr2:
            print(i,end=" ")
    print()
