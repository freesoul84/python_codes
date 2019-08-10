test=int(input())
for _ in range(test):
    n,ele=map(int,input().split())
    array=list(map(int,input().split()))
    if ele in array:
        print(array.index(ele))
    else:
        print(-1)
