array=[12,5456,8776,867,243]
value=len(list(min(array)))
for i in array:
    a=list(i//10)
    val=int(''.join(a))
    print(val)    
