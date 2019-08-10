#code for Multiply left and right array sum.
conditions=int(input())
for _ in range(conditions):
    size=int(input())
    array=list(map(int,input().split()))
    split=size//2
    a=array[:split]
    b=array[split:]
    sum1=sum(a)
    sum2=sum(b)
    result=sum1*sum2
    print(result)
