test=int(input())
for _ in range(test):
    num=int(input())
    array=list(map(int,input().split()))
    val=set(array)
    while len(val)>0:
        min1=min(val)
        count1=array.count(min1)
        for i in range(1,count1+1):
            print(min1,end=" ")
        val.remove(min1)
    print()
