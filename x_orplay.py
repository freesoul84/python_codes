test=int(input())
for  i in range(test):
    number=int(input())
    res=0
    for i in range(1,number):
        val=number%i
        if val==0:
            res=res ^ i

    print(res)
