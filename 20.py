# Write a program to generate a sequence of 
# numbers using generator functions and yield 
# keyword. 


def abc(n):
    while n > 0:
        yield n
        n-=1
for n in abc(5):
    print(n)