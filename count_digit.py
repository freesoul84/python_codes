test=int(input())
for _ in range(test):
    num=int(input())
    temp,c=num,0
    while num>0:
        r=num%10
        if r>0:
            if temp%r==0:
                c+=1
        num=num//10
    print(c)
