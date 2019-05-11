import math
test=int(input())
for _ in range(test):
    number=int(input())
    array=list(map(int,input().split()))
    val=int(math.ceil(number//2))
    if array[val]==1 and array[val-1]>1 and array[val+1]>1:
        sum1=sum(array[:val])
        sum2=sum(array[val+1:])
        if sum1==sum2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
