#play with an array
test=int(input())
for _ in range(test):
    number=int(input())
    array=list(map(int,input().split()))
    odd=[]
    even=[]
    for i in range(array):
        if array[i]%2==0:
            even.append(array[i])
        else:
            odd.append(array[i])
    e,o=0,0
    for i in range(len(array)):
        if i%2==0:
            array[i]=even[e]
            e+=1
        else:
            array[i]=odd[o]
            o+=1
