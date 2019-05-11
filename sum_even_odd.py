test=int(input())
for _ in range(test):
    number=int(input())
    sum1,sum2=0,0
    for i in range(1,number+1):
        if i%2==0:
            sum1+=i
        elif i%2==1:
            sum2+=i

    print(str(sum1)+" "+str(sum2))
