test=int(input())
for _ in range(test):
    number=int(input())
    res=""
    while number>0:
        reminder=number%10
        if reminder==0:
            res+=str(5)
        else:
            res+=str(reminder)
        number=number//10

    a=''.join(list(reversed(res)))
    print(a)
