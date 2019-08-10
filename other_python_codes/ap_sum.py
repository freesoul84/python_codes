test=int(input())
for _ in range(test):
    number=int(input())
    array=[i for i in range(1,number+1,1)]
    a=array[0]
    d=array[1]-array[0]
    result=int((number/2)*(2*a+(number-1)*d))
    print(result)
