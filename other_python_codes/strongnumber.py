def factorial(number):
    if number<=1:
        fact=number
    else:
        fact=number*factorial(number-1)
    return fact
test=int(input())
for _ in range(test):
    number=int(input())
    sum1=0
    temp=number
    while number>0:
        reminder=number%10
        sum1+=factorial(reminder)
        number=number//10

    if sum1==temp:
        print("Strong")
    else:
        print("Not Strong")
