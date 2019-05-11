from collections import Counter
test=int(input())
for _ in range(test):
    num=int(input())
    array=list(map(int,input().split()))
    count=Counter(array)
    count=sorted(array,key=lambda a:(count[a],-a),reverse=True)
    print(*count)
