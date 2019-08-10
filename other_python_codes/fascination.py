test=int(input())
digits=[1,2,3,4,5,6,7,8,9]
for _ in range(test):
    number=int(input())
    if len(str(number))>=3:
        value1=number*2
        value2=number*3
        result=list(map(int,list(str(number)+str(value1)+str(value2))))
        co=0
        for i in result:
            if i in digits and result.count(i)==1:
                co+=1

        if co==len(result):
            print(1)
        else:
            print(0)
