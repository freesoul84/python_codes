from sys import maxsize
test=int(input())
for _ in range(test):
    number=int(input())
    array=list(map(int,input().split()))
    max_so_far =a[0]
    curr_max = a[0]
    for i in range(1,size):
        curr_max = max(a[i],curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)

    print(max_so_far)
