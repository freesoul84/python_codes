test=int(input())
for _ in range(test):
    num=int(input())
    temp=num
    val=[]
    while num>0:
        r=num%10
        if r==6:
            val.append(str(9))
        else:
            val.append(str(r))
        num=num//10
    val1=int(''.join(list(reversed(val))))
    diff =val1-temp
    print(diff)
