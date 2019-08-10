from collections import OrderedDict
t=int(input())
for i in range(t):
    s=input()
    d=OrderedDict()
    f=1
    for ch in s:
        d[ch]=d.get(ch,0)+1
    for item in d:
        if d[item]>1:
            print(item)
            f=0
            break
    if f!=0:
        print("-1")
    print(d)
