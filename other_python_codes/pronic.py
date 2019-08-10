test=int(input())
for _ in range(test):
    num=int(input())
    for i in range(num+1):
        val=i
        i+=1
        res=val*i
        print(res,end=" ")
        if res==num:
            break
    print()    
