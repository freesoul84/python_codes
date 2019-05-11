test=int(input())
for _ in range(test):
    number=int(input())
    array=list(map(int,input().split()))
    sum=0
    avg=0
    for i in range(0,len(array)):
        sum+=array[i]
        avg=sum//(i+1)
        print(avg,end=" ")
    print()
