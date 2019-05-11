test=int(input())
for i in range(test):
    a,b=map(int,input().split(' '))
    array=list(map(int,input().split(' ')))
    for i in range(array):
        diff1=abs(array[i]-b)
        j=i+1
        for j in range(array):
            diff2=abs(array[j]-diff1)
            if diff2 in array:
                print()
