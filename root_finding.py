#program to find the nth root of m number
test=int(input())
from sys import stdin,stdout
for i in range(test):
    m,n=map(int,stdin.readline().split(' '))
    value=[]
    while m>1:
        value.append(n)
        m=int(m//n)

