# 9. Write a program to demonstrate iterators and 
# iterables in Python. 


#iterators
l = iter([1,2,3,4])
print("iterators")
print(next(l))
print(next(l))
print(next(l))
print(next(l))

#iterables
l=[1,2,3,4]
print("iterables")
for i in l:
    print(i)
    
    
#iterables = l=[1,2,3,4]
#iterators = is loop and iter()

