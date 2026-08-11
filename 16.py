# 6. Write a program to iterate over lists strings and 
# dictionaries using loops. 

l=[11,22,33,44,55]

s="jalpit"

d={
  1:"a",  
  2:"b",  
  3:"c",  
  4:"d"  
}

print("iterateing list")
for i in l:
    print(i)
    
print("iterateing string")
for i in s:
    print(i)
    
print("iterateing dictionaries")
for i,j in d.items():
    print("key:",i,"val:",j)