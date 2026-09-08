# Write a program to perform file and directory 
# operations using os and sys modules. 
import sys
import os

print('sys version:',sys.version)


if not os.path.isdir('testdir'):
    os.makedirs('testdir')
    
if os.path.isfile('test.txt'):
    os.rename('test.txt','0.py')    
    os.remove('0.py')
    

print(os.path.isabs('C:\\jalpit-4029\\python\\26.py'))
print(os.path.basename('C:\\jalpit-4029\\python\\26.py'))

