test=int(input())
for _ in range(test):
    num,k=map(int,input().split())
    array=list(map(int,input().split()))
    stack=[]
    for i in range(num):
        if i<k:
            stack.append(array[i])
    i=k
    while i>0:
        print(stack.pop(),end=" ")
        i-=1

    for i in array[k:]:
        print(i,end=" ")

    print()
