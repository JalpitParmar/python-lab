#  Write a program to demonstrate basic regular 
# expression pattern matching. 
import re

s = input("Enter the email: ")

regular_expression = re.compile(r'\@\w+\.com')

ans  = regular_expression.search(s)

if ans == None:
    print("not a valid email")
else:
    print("email: ",s)