
def bin_search(arr,l,r,k):
    if r>=l:
        mid=l+(r-l)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return bin_search(arr,l,mid-1,k)
        elif arr[mid]< k:
            return bin_search(arr,mid + 1,r,k)
    else:
        return -1

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        x=int(input())
        print(bin_search(arr,0,len(arr)-1,x))
