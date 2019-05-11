import math
test=int(input())
for _ in range(test):
    num=int(input())
    root=math.sqrt(num)
    ceiling=math.ceil(root)
    floor=math.floor(root)
    if floor!=ceiling:
        diff1=ceiling**2-num
        diff2=num**2-floor
        if diff1<diff2:
            print(str(ceiling**2)+" "+str(diff1))
        else:
            print(str(floor**2)+" "+str(diff2))
    else:
        print()
