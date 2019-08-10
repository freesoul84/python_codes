test=int(input())
from sys import stdin,stdout
for i in range(test):
    a,b=map(int,stdin.readline().split())
    array=[]
    v1,v2=a,b
    min1=min(v1,v2)
    while min1>=1 and a>=1 and b>=1:
        array.append(a*b)
        a-=1
        b-=1
    print(sum(array))