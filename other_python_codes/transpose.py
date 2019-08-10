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

    res = [[a[j][i] for j in range(num)] for i in range(len(a[0]))]

    for row in res:
        for i in row:
            print(i,end=" ")
    print()
