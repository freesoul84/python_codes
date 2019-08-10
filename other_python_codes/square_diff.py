test=int(input())
for _ in range(test):
    num=int(input())
    a=num*(num+1)/2
    sum1=a*a
    sum2=num*(num+1)*(2*num+1)/6
    diff=sum1-sum2
    print(int(diff))
