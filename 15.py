# 5. Write a program to demonstrate the use of 
# break continue and pass statements. 

print("break statements")
for i in range(1,6):
    if i == 3:
        break
    print(i)
    
print("continue statements")
for i in range(1,6):
    if i == 3:
        continue
    print(i)
    

print("pass statements")
for i in range(1,6):
    if i == 3:
        pass
    print(i)