test=int(input())
for i in range(test):
    string1=str(input())
    for i in string1:
        if i.isdigit():
            print(i,end="")
        else:
            print(-1)
            break
    print()
