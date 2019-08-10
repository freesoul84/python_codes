test=int(input())
for _ in range(test):
    number=int(input())
    if number>9:
        count=9
        for i in range(10,number+1):
            while i > 0:
                r=i%10
                count+=1
                i=i//10
        print(count)
    elif number<=9:
        print(number)
