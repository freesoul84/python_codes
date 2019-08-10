test=int(input())
for _ in range(test):
    n=int(input())
    i=1
    while n>0:
        n=n-999*i
        print(n)
        i+=1
    if n==0:
        print("Divisible")
    else:
        print("Not Divisible")
