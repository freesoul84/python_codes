test=int(input())
for _ in range(test):
    number=int(input())
    temp=number
    while temp>0:
        for i in range(number,0,-1):
            print(str(i)*temp,end="")
        print("$",end="")
        temp-=1
    print()
