vowels=['a','e','i','o','u','A','E','I','O','U']
test=int(input())
for _ in range(test):
    string1=str(input())
    s1=[]
    for i in range(len(string1)):
        if  string1[i]  not in vowels:
            if string1.count(string1[i])==1:
                s1.append(string1[i])
    lens1=len(set(s1))
    if len(s1)%2==0:
        print("SHE!")
    else:
        print("HE!")
