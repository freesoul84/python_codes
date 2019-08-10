test=int(input())
for _ in range(test):
    num,k=list(map(int,input().split()))
    array=list(map(int,input().split()))
    val=[]
    for i in range(num,k):
        val+=reversed(array[i:k])
