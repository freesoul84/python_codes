import math
test=int(input())
for _ in range(test):
    a,b,c=map(int,input().split())
    s=(a+b+c)/2
    result=math.sqrt(abs((s*(s-a)*(s-b)*(s-c))))
    print("{0:6f}".format(result))
