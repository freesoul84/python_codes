import math
test=int(input())
for _ in range(test):
    num=int(input())
    num1=math.ceil(math.sqrt(num))
    count=0
    for i in range(1,num1):
        if i**2<num:
            count+=1
    print(count)
