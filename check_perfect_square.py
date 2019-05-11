import math
for _ in range(int(input())):
    number=int(input())
    value=math.log10(number)/math.log10(2)
    if math.ceil(value)==math.floor(value):
        print("YES")
    else:
        print("NO")
