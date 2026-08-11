a=int(input("Enter val A:"))
b=int(input("Enter val B:"))
o = input("Eneter opration(+,-,*,/):") 
 


def clu(a,b,o):
    if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*":
        return a*b
    elif o=="/":
        return a/b
    else:
        return "invalid opration it must be (+,-,*,/)"
    

print(clu(a,b,o))