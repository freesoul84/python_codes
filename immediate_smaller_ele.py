test=int(input())
for _ in range(test):
    number=int(input())
    array=list(map(int,input().split()))
    for i in range(number-1):
        if array[i]>array[i+1]:
            array[i]=array[i+1]
        else:
            array[i]=-1
    array[-1]=-1

    for i in range(number):
        print(array[i],end=" ")
    print()
