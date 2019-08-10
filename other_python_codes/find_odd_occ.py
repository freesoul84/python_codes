test=int(input())
for _ in range(test):
    num=int(input())
    array=list(map(int,input().split()))
    hashmap={}
    for i in array:
        count1=array.count(i)
        if count1%2==0:
            hashmap[i]=True
            print(hashmap)
    for i in set(array):
        if i not in hashmap:
            print(i,end=" ")
    print()
