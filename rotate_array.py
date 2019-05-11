test=int(input())
for i in range(test):
    a,b=map(int,input().split())
    array=list(map(int,input().split()))
    value=array[b:]+array[:b]
    for i in range(len(value)):
        print(value[i],end=" ")
    print()
