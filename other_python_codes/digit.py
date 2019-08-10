def digits(number):
    temp=number
    if temp<10:
        return temp
    else:
        sum1=0
        while number>0:
            reminder=number%10
            sum1+=reminder
            number=number//10
        result=digits(sum1)

    return result

print(digits(999999999999999999995))
