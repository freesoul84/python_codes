test=int(input())
for _ in range(test):
    string2=str(input())
    len1=len(string2)-1
    while len1>=0:
        if int(string2[len1])==1:
            print(len1)
            break
        len1-=1
    else:
        print(-1)
