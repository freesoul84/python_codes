test=int(input())
for i in range(test):
    num,check=map(int,input().split())
    array=list(map(int,input().split()))
    a,b=0,0
    for i in range(num):
        if array[i]<=check:
            a+=1
        if array[i]>=check:
            b+=1
    print(str(a)+" "+str(b))
