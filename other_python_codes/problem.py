
#function defination
def sum_cal():
    sum=0
    #range from 1 to 999
    for i in range(1,1000):
        if i%3==0 or i%5==0:
            sum+=i
    
    return sum

#function calling
sum=sum_cal()
#printing of function
print(sum)
