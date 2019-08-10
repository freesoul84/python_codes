test=int(input())
for _ in range(test):
    number=int(input())
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count+=1
        if count==3:
            print(1)
            break
    if count!=3:
        print(0)
