test=int(input())
for _ in range(test):
    number=int(input())
    array=list(map(int,input().split()))
    count=0
    for i in array:
        j=len(i)-1
        for i in range(len(array)):
            if array[i]==array[j]:
                j-=1
                continue
            else:
                break
        else:
            count+=1

    if count==len(array):
        print(1)
    else:
        print(0)
