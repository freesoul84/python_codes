test=int(input())
def binary_search(array,l,n,k):
    mid=(l+n)//2
    if array[mid]==k:
        return mid
    elif array[mid]>k:
        l=mid+1
        binary_search(array,l,n,k)
    elif array[mid]<k:
        n=mid-1
        binary_search(array,l,n,k)
for _ in range(test):
    n=int(input())
    array=list(map(int,input().split()))
    k=int(input())
    l=0
    print(binary_search(array,l,n,k))
