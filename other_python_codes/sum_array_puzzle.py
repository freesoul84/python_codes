test=int(input())
for _ in range(test):
    num=int(input())
    array=list(map(int,input().split()))
    for i in range(num):
        sum1=sum(array)-array[i]
        print(sum1,end=" ")
    print()
