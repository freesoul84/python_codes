test=int(input())
for _ in range(test):
    number=int(input())
    array=list(map(int,input().split()))
    for i in range(number):
        if i+2>(number-1):
            break
        array[i],array[i+2]=array[i+2],array[i]

    for i in range(number):
        print(array[i],end=" ")
    print()
