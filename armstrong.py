#calculate the sum of a number where each digit is powered to number of digit(armstrong)
x=1634
y=x
length=0
while(y>0):
    length+=1
    y=y//10
print(length) 
sum=0
while(x>0):
    rem=x%10
    sum+=rem**length
    x=x//10
print(sum)    
       