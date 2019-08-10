test=int(input())
def flood_fill(array,a,b,val):
    temp=array[a][b]
    array[a][b]=val
    if array[a+1][b]==temp:
        flood_fill(array,a+1,b,val)
    elif(array[a,b-1]):
        flood_fill(array,a,b-1,val)
    elif(array[])
import numpy as np
for _ in range(test):
    m,n=map(int,input().split(' '))
    array=np.array(list(map(int,input().split(' '))))
    array1=[]
    array=array.reshape(m,n)
    a,b,val=int(input())
