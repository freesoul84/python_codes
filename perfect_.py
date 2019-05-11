test=int(input())
def fact(n):
    if n<2:
        f=1
    else:
        f=n*fact(n-1)
    return f
for _ in range(test):
    number=int(input())
    sum1=0
    temp=number
    while number>0:
        r=number%10
        sum1+=fact(r)
        number=number//10
    if sum1==temp:
        print("Perfect")
    else:
        print("Not Perfect")
