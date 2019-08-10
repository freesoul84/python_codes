test=int(input())
for _ in range(test):
    num=int(input())
    binary=str(bin(num)).count('1')
    print(binary)
