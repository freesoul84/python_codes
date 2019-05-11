test=int(input())
for i in range(test):
    n=int(input())
    for i in range(0,n+1):
        if i%10==i or i==10:
            print(i,end=" ")
        if len(str(i))>1:
            temp=i
            print(temp)
            c=0
            while(i>0):
                r1=i%10
                a=i//10
                r2=a%10
                print("i",i)
                print("r1",r1)
                print("r2",r2)
                if abs(r2-r1)==1:
                    c+=1
                else:
                    break
                i=i//10
            if c==len(str(temp))-1:
                print(temp,end=" ")
