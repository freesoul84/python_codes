test=int(input())
for i in range(test):
    n=int(input())
    array=list(map(int,input().split()))
    c=0
    val=max(array)
    for i in range(val):
        for j in range(n):
            if array[j]>0:
                array[j]=array[j]-1
        c+=1

    print(c)
