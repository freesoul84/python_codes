def powercheck(num):
    v=num and (not(num & (num - 1)))
    if v:
        return "YES"
    else:
        return "NO"
test=int(input())
for _ in range(test):
    number=int(input())
    print(powercheck(number))
