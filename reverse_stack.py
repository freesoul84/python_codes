test=int(input())
for _ in range(test):
    string=str(input())
    stack=[]
    for i in string:
        stack.append(i)

    for i in range(len(string)):
        print(stack.pop(),end="")
    print()
