test=int(input())
for _ in range(test):
    number=str(int(input()))
    sum1,sum2=0,0
    for i in range(len(number)):
        if i%2==0:
            sum1+=int(number[i])
        else:
            sum2+=int(number[i])

    if abs(sum2-sum1)==0:
        print("Yes")
    else:
        print("No")
