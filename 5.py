'''5. Write a program to create and manipulate lists 
using indexing slicing and list comprehensions. '''

text = ['apple','banana',10,'cherry','orange',20,'grapes','kiwi']

print(text[0:7])
print(text[:7])
print(text[5:])
print(text[::2])
print(text[::-1])
print(text[:-1])
print(text[1:6:2])

print()

text.pop(2)
print(text)

print()

text.append("lemon")
print(text)

print()

text.reverse()
print(text)

print()

text.clear()
print(text)





