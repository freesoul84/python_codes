test=int(input())
for _ in range(test):
    num=int(input())
    array=list(map(int,input().split()))
    c=0
    a=[]
    for i in range(num):
        val=[]
        for j in range(num):
            val.append(array[c])
            c+=1
        a.append(val)

    sum1=0
    sum2=0
    for i in range(num):
        for j in range(num):
            if i==j:
                sum1+=a[i][j]
            if i+j==num-1:
                sum2+=a[i][j]

    print(abs(sum2-sum1))
