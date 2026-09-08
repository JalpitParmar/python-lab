# Write a program to copy move and delete files 
# using shut il module. 

import shutil
import os

if os.path.isfile('1.py'):
    if not os.path.isdir('testdir'):
        os.makedirs('testdir')
    shutil.copy('1.py','testdir')
    if not os.path.isdir('xyz'):
        os.makedirs('xyz')
    shutil.move('C:\\jalpit-4029\\python\\testdir\\1.py','xyz')
    
    os.remove('xyz\\1.py')