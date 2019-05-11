test=int(input())
for _ in range(test):
    num,a,b=map(int,input().split())
    array=list(map(int,input().split()))
    c=0
    for i in range(a,b+1,1):
        if i in array:
            c+=1
            continue
        else:
            print("No")
            break
    if c==(b-a)+1:
        print("Yes")
