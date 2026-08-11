
n = int(input("Enter val:"))
ans = 1

#simpal factorial 
for i in  range(1,n+1):
    ans*=i
    
print(ans)

#recursion factorial

def fac(n):
    if n == 1 or n ==0:
        return 1
    return n * fac(n-1)

print(fac(n))

#simpal Fibonacci
a=0
b=1

for i in range(n):
    a,b = b,a+b
print(b)

#recursion Fibonacci

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(n))
