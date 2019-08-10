#sum of elements to find its AP
test=int(input())
for _ in range(test):
    a,d,n=map(int,input().split())
    result=(n/2)*(2*a+(n-1)*d)
    print(result)
