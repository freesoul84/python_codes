#find the sum of n numbers who are multiply by 3 or 7
test=int(input())
for _ in range(test):
    number=int(input())
    sum1=0
    for i in range(1,number+1):
        if i%3==0 or i%7==0:
            sum1+=i

    print(sum1)
