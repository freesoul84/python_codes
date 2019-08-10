test=int(input())
for _ in range(test):
    num=int(input())
    binary=str(bin(num))
    for i in range(len(binary)-1,0,-1):
        if binary[i]=='1':
            print(len(binary)-i)
            break
    else:
        print(0)
