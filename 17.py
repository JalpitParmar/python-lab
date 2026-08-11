# 7. Write a program to demonstrate list dictionary 
# and set comprehensions.

print("list is mutable")
l=[1,2,3,4,5,6,7,8,9]
print(type(l))
print("list",l)
l.append(10)
print("val added",l)
l.remove(10)
print("val removed",l)


print("="*50)
print("set is mutable")
s={5,6,2,4,3,1,8,7,9}
print(type(s))
print("set",s)
s.add(10)
print("val added",s)
s.remove(10)
print("val removed",s)

print("="*50)
print("dec is mutable")
d={1:"a",2:"b",3:"c"}
print(type(d))
print("dec",d)
d[4]="d"
print("val added",d)
d.pop(4)
print("val removed",d)

