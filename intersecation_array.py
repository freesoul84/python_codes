test=int(input())
for _ in range(test):
    size1,size2=map(int,input().split())
    array1=set(map(int,input().split()))
    array2=set(map(int,input().split()))
    result=array1.intersection(array2)
    if len(result):
        for i in sorted(result):
            print(i,end=" ")
        print()
    else:
        print(0)
        print()
