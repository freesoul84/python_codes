
test=int(input())
alpha=set(['a','e','i','o','u','A','E','I','O','U'])
for _ in range(test):
    string1=input()
    for i in string1:
        if i in alpha:
            print(i,end="")
