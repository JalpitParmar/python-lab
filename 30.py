# .Write a program to extract specific information 
# from a text file using regular expressions. 

import re

with open('txt.txt','r') as f:
    txt = f.read()
    regular_expression = re.compile(r'\w+a\w+')
    ans = regular_expression.findall(txt)
    print(ans)