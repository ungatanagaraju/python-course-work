Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="Nagaraju is learning python course"
s.startswith("N")
True
s.startswith("A")
False
s.endwith("ourse")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.endwith("ourse")
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
s.endwiths("course")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.endwiths("course")
AttributeError: 'str' object has no attribute 'endwiths'. Did you mean: 'endswith'?
s.endswith("course")
True
s.endswith(".ing")
False

s.isalpha()
False
'dsfasfasd'.isalpha()
True
' '.isalpha()
False
'python3'.isalpha()
False
'Python'.isalpha()
True
'Python'.isalnum()
True
'123456'.isalnum()
True
'python'.isalnum()
True
'python 123'.isalnum()
False
'python.123'.isalnum()
False
'p'.islower()
True
'pyhton'.isupper
<built-in method isupper of str object at 0x00000237DC092520>
'pyhton'.isupper()
False
'PYTHON'.isupper()
True
'pyhton123'.islower()
True
'pyhton  123'.islower()
True
'    '.isspace()
True
'pyhton 123'.isspace()
False
s
'Nagaraju is learning python course'
s.title()
'Nagaraju Is Learning Python Course'
s.istilte()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s.istilte()
AttributeError: 'str' object has no attribute 'istilte'. Did you mean: 'istitle'?
s.istitle()
False
'123dfgfhf'.isidentifier()
False
'if'.isidentifier()
True
if=12
SyntaxError: invalid syntax
s
'Nagaraju is learning python course'
'12.3'.isdecimal()
False
'123'.isdecimal()
True
'12345'.isdigit()
True
'345865423'.isnumeric()
True
l=[]
type(l)
<class 'list'>
l-list()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l-list()
TypeError: unsupported operand type(s) for -: 'list' and 'list'
l=list()
l
[]
type(l)
<class 'list'>
l=list()
l
[]
type(l)
<class 'list'>
l=[6,9.0,"gdfgdafg",[],{},{1:},True]
SyntaxError: expression expected after dictionary key and ':'
l=[6,9.0,"gdfgdafg",[],{},{1:5},True]
l
[6, 9.0, 'gdfgdafg', [], {}, {1: 5}, True]
a=[1,2,3,4]
b[5,6,7,8]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    b[5,6,7,8]
NameError: name 'b' is not defined
b=[5,6,7,8]
a+b
[1, 2, 3, 4, 5, 6, 7, 8]
a*8
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
ab*3
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    ab*3
NameError: name 'ab' is not defined. Did you mean: 'a'?
a*2b*3
SyntaxError: invalid decimal literal
a*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
a*3+b*2
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 5, 6, 7, 8]
names=['asif','nagaraju','sameer','priya','mahitha','bavana']
names=['asif','nagaraju','sameer','priya','mahitha','bavana']
names[0]
'asif'
name[1]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    name[1]
NameError: name 'name' is not defined. Did you mean: 'names'?
names[1]
'nagaraju'
names[5]
'bavana'
names[-1]
'bavana'
names[::2]
['asif', 'sameer', 'mahitha']
['asif', 'sameer', 'mahitha']
['asif', 'sameer', 'mahitha']
names[1:3]
['nagaraju', 'sameer']
name[:-1]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    name[:-1]
NameError: name 'name' is not defined. Did you mean: 'names'?
names=[:-1]
SyntaxError: invalid syntax
names=[::-1]
SyntaxError: invalid syntax
names
['asif', 'nagaraju', 'sameer', 'priya', 'mahitha', 'bavana']
names=[::-1]
SyntaxError: invalid syntax
names[::-1]
['bavana', 'mahitha', 'priya', 'sameer', 'nagaraju', 'asif']
names[::-3]
['bavana', 'sameer']
len(names)
6
sorted(names)
['asif', 'bavana', 'mahitha', 'nagaraju', 'priya', 'sameer']
name[0]='conquest'
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    name[0]='conquest'
NameError: name 'name' is not defined. Did you mean: 'names'?
name
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    name
NameError: name 'name' is not defined. Did you mean: 'names'?
names
['asif', 'nagaraju', 'sameer', 'priya', 'mahitha', 'bavana']
id(names)
2438938207424
name[0]='Asif'
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    name[0]='Asif'
NameError: name 'name' is not defined. Did you mean: 'names'?
names
['asif', 'nagaraju', 'sameer', 'priya', 'mahitha', 'bavana']
names[0]='Asif'
names
['Asif', 'nagaraju', 'sameer', 'priya', 'mahitha', 'bavana']
names[1]='sameer'
names
['Asif', 'sameer', 'sameer', 'priya', 'mahitha', 'bavana']
id(names)
2438938207424
\
names
['Asif', 'sameer', 'sameer', 'priya', 'mahitha', 'bavana']
names.append('Abhiram')
names
['Asif', 'sameer', 'sameer', 'priya', 'mahitha', 'bavana', 'Abhiram']
names.insert('Rajesh')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    names.insert('Rajesh')
TypeError: insert expected 2 arguments, got 1
name
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    name
NameError: name 'name' is not defined. Did you mean: 'names'?
names.insert(3,"Rajesh")
names
['Asif', 'sameer', 'sameer', 'Rajesh', 'priya', 'mahitha', 'bavana', 'Abhiram']
names.extend(['yaswanth','dheshik','saikran'])
name
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    name
NameError: name 'name' is not defined. Did you mean: 'names'?
na,names
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    na,names
NameError: name 'na' is not defined. Did you mean: 'a'?
names
['Asif', 'sameer', 'sameer', 'Rajesh', 'priya', 'mahitha', 'bavana', 'Abhiram', 'yaswanth', 'dheshik', 'saikran']
names
['Asif', 'sameer', 'sameer', 'Rajesh', 'priya', 'mahitha', 'bavana', 'Abhiram', 'yaswanth', 'dheshik', 'saikran']
names.pop(0)
'Asif'
names
['sameer', 'sameer', 'Rajesh', 'priya', 'mahitha', 'bavana', 'Abhiram', 'yaswanth', 'dheshik', 'saikran']
names.pop()
'saikran'
names
['sameer', 'sameer', 'Rajesh', 'priya', 'mahitha', 'bavana', 'Abhiram', 'yaswanth', 'dheshik']
names.pop(3)
'priya'

names
['sameer', 'sameer', 'Rajesh', 'mahitha', 'bavana', 'Abhiram', 'yaswanth', 'dheshik']
del names()
SyntaxError: cannot delete function call
names.remove('Asif')
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    names.remove('Asif')
ValueError: list.remove(x): x not in list
names.remove('Nagaraju')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    names.remove('Nagaraju')
ValueError: list.remove(x): x not in list
names.remove('sameer')
name
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    name
NameError: name 'name' is not defined. Did you mean: 'names'?
names
['sameer', 'Rajesh', 'mahitha', 'bavana', 'Abhiram', 'yaswanth', 'dheshik']
del.names()
SyntaxError: invalid syntax
del names()
SyntaxError: cannot delete function call
del names[]
SyntaxError: invalid syntax
del names[3]
names
['sameer', 'Rajesh', 'mahitha', 'Abhiram', 'yaswanth', 'dheshik']
names.clear()

name
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    name
NameError: name 'name' is not defined. Did you mean: 'names'?
names
[]
names.pop()
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    names.pop()
IndexError: pop from empty list
names=['Asif', 'sameer', 'sameer', 'Rajesh', 'priya', 'mahitha', 'bavana', 'Abhiram', 'yaswanth', 'dheshik', 'saikran']
names
['Asif', 'sameer', 'sameer', 'Rajesh', 'priya', 'mahitha', 'bavana', 'Abhiram', 'yaswanth', 'dheshik', 'saikran']
 names.index('mehaboob')
 
SyntaxError: unexpected indent
names.index('mehaboob')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    names.index('mehaboob')
ValueError: list.index(x): x not in list
names.index('Rajesh')
3
names.index('dheshik')
9
names
['Asif', 'sameer', 'sameer', 'Rajesh', 'priya', 'mahitha', 'bavana', 'Abhiram', 'yaswanth', 'dheshik', 'saikran']
names.index('Z')
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    names.index('Z')
ValueError: list.index(x): x not in list
l=[1,,1,1,23,12,13,]
SyntaxError: invalid syntax
l=[1,1,1,23,12,13,]
l.count(1)
3
l.count(6)
0
sorted(l)
[1, 1, 1, 12, 13, 23]
s
'Nagaraju is learning python course'
set()
set()
l
[1, 1, 1, 23, 12, 13]
l.sort()
l
[1, 1, 1, 12, 13, 23]
l.sort()
l
[1, 1, 1, 12, 13, 23]
l.sort(reverse=True)
l
[23, 13, 12, 1, 1, 1]
l.reverse()
l
[1, 1, 1, 12, 13, 23]
l
[1, 1, 1, 12, 13, 23]
a=[1,2,3,4,5]
b=a
b
[1, 2, 3, 4, 5]
c=a.copy()
id(a)
2438938260736
id(b)
2438938260736
\
id(c)
2438938256960
>>> c
[1, 2, 3, 4, 5]
>>> b.append(10)
>>> b
[1, 2, 3, 4, 5, 10]
>>> b.append(14)
>>> b
[1, 2, 3, 4, 5, 10, 14]
>>> a
[1, 2, 3, 4, 5, 10, 14]
>>> sum(a)
39
>>> len(a)
7
>>> #[0,0.0,'',[],{},set(),(),False]
>>> #[1,-1,0.1,'faffgfdg',[123],]
>>> any([0,0.0,'',[],{},set(),(),False])
False
>>> any([1,0,0.0,'',[],{},set(),(),False])
True
>>> all([1,0,0.0,'',[],{},set(),(),False])
False
>>> all([1,0,0.1,'',[123],{},set(),(),False])
False
