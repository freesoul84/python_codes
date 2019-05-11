test=int(input())
for _ in range(test):
    num=int(input())
    sum1=0
    c=0
    for i in range(2,((num)*2)+1,2):
        if c>=num:
            break
        sum1+=i**2
        c+=1
    print(sum1)
