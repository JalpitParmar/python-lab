# 4. Write a program to find the sum of digits of a 
# number using a while loop. 

n = int(input("Enter val:"))


sum=0
while n!=0:
    sum+=n%10
    n=n//10
print("sum of digits",sum)
    