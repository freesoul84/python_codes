test=int(input())
for _ in range(test):
    number=int(input())
    sum1=0
    for i in range(1,number+1):
        sum1+=i**3

    print(sum1)
