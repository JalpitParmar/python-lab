# Write a program to use re module functions 
# such as match search and find all. 

import re

s = input("Enter list of string:(mat cat bat):")

regular_expression = re.compile(r'\w+a\w+')

print(regular_expression.findall(s))
print(regular_expression.search(s).group())