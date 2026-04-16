# This program calculates the area of a rectangle
length =10
width =5
area =length*width
if area >30:
    print("Large area")
else:
    print("small area")
    
# Statement
x=10      #Assigment statement
print(x)  #Function call statement

#Identifier
age = 25        #'age' is an identifier(valid)
_name = "john"  #'_name is a valid identifier
score1=88       # valid:letters + digits

#Invalid examples(will cause error if uncommunted)
#1age=30        #Invalid:starts with a digit
#def =5         #Invalid: 'def' is a python keyword

# This is a single-line comment
x = 10 # This is also a comment

''' This is a multi-line comment.
It spans multiple lines.
'''
print("Hello, World!")

import keyword

print(keyword.kwlist) # List of all keywords
print(len(keyword.kwlist)) # Total number of keywords

product_name = "Laptop"
price = 45000
in_stock = True
print(product_name, price, in_stock)

a, b, c = 10, 20, 30
print(a, b, c) # Output: 10 20 30

x = y = z = 100
print(x, y, z) # Output: 100 100 100

x = 5
x = 10
print(x) # Output: 10

a, b = 5, 10
a, b = b, a
print(a, b) # Output: 10 5

x = 100
del x
# print(x) # Raises: NameError: name 'x' is not defined


















