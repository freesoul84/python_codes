test=int(input())
for _ in range(test):
    number=int(input())
    fib=[0]*number
    if number>=2:
        fib[0]=0
        fib[1]=1
        for i in range(2,number):
            fib[i]=fib[i-1]+fib[i-2]
        print(fib[number-1])

    else:
        print(number)
