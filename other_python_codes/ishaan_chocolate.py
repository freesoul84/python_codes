#Ishaan Loves Chocolates
from sys import stdin,stdout
test=int(input())
for i in range(test):
    number=int(input())
    array=list(map(int,stdin.readline().split(' ')))
    for i in range(len(array)-1):
        array.remove(max(array))
    print(array[0])
