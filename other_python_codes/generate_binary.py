# test=int(input())
# for _ in range(test):
#     n=int(input())
#     for i in range(1,n+1):
#         v=""
#         while i>0:
#             r=i%2
#             i=i//2
#             v+=str(r)
#         v=''.join(list(reversed(v)))
#         print(v,end=" ")
#     print()
import queue
def binaryg(n):
    q=queue.Queue()
    q.put("1")
    while(n>0):
        a=q.get()
        print(a,end=" ")
        b=a
        q.put(a+"0")
        q.put(b+"1")
        n-= 1
n = 10

test=int(input())
for _ in range(test):
    n=int(input())
    binaryg(n)
    print()
