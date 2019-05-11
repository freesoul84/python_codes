test=int(input())
for i in range(test):
    number=int(input())
    array=list(map(int,input().split()))
    result=1
    for i in array:
        result*=i

    print(result)
