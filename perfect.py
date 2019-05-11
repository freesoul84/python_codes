test=int(input())
for _ in range(test):
    num=int(input())
    array=list(map(int,input().split()))
    j=len(array)-1
    for i in range(len(array)):
        if array[i]==array[j]:
            j-=1
            continue
        else:
            print("NOT PERFECT")
            break
    else:
        print("PERFECT")
