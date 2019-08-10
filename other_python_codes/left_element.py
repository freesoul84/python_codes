#left element in array
test=int(input())
for _ in range(test):
    number=int(input())
    array=list(map(int,input().split()))
    for i in range(len(array)-1):
        if i%2==0:
            array.remove(max(array))
        else:
            array.remove(min(array))

    print(array[0])
