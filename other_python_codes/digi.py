test=int(input())
for _ in range(test):
    number,base=map(int,input().split())
    a=[]
    while number>0:
        r=number%base
        a.append(str(r))
        number=number//base

    print(''.join(reversed(a)))
