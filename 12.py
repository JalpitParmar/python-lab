# 2. Write a program to check whether a number is 
# positive negative or zero using nested 
# conditions. 

n = int(input("Enter val:"))

if n>0:
    if n!=0:
        print("positive")
    else:
        print("zero")
else:
    if n!=0:
        print("negative")
    else:
        print("zero")