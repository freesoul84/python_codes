test=int(input())
for _ in range(test):
    num=int(input())
    string1=str(input())
    j=num-1
    for i in range(num):
        if string1[i]==string1[j]:
            j-=1
            continue
        else:
            print("No")
            break
    else:
        print("Yes")
