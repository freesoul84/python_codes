test=int(input())
for _ in range(test):
    num=int(input())
    sum1=sum([i**2 for i in range(1,num*2,2)])
    print(sum1)
