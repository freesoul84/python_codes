test=int(input())
for _ in range(test):
    num_bin=str(int(input()))
    c,sum1=0,0
    for i in range(len(str(num_bin))-1,-1,-1):
        a=num_bin[i]
        if a==str(1):
            sum1+=int(a)*(2**c)
        c+=1

    print(sum1)
