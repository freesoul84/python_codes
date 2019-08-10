test=int(input())
for _ in range(test):
    num=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    hashmap={}
    for i in arr1:
        if i not in hashmap:
            hashmap[i]=True

    for j in arr2:
        if j not in hashmap:
            print(0)
            break
    else:
        print(1)
