test=int(input())
import math
for _ in range(test):
    number=int(input())
    value=math.sqrt(number)
    if value==math.floor(value):
        print(1)
    else:
        print(0)
