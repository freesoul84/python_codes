test=int(input())
for _ in range(test):
    array1=list(map(int,input().split()))
    array2=list(map(int,input().split()))
    a,b=0,0
    for i in range(len(array1)):
        if array1[i]>array2[i]:
            a+=1
        elif array1[i]<array2[i]:
            b+=1

    print(str(a)+" "+str(b))
    print()
