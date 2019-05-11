test=int(input())
for _ in range(test):
    num=int(input())
    array=list(map(int,input().split()))
    a=[]
    c=0
    for i in range(num):
        val=[]
        for j in range(num):
                val.append(array[c])
                c+=1
        if i%2==1:
            a.append(list(reversed(val)))
        else:
            a.append(list(val))


    for i in range(num):
        for j in range(num):
            print(a[i][j],end=" ")

    print()
