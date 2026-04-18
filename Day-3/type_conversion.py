Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
folat(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    folat(a)
NameError: name 'folat' is not defined. Did you mean: 'format'?
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
tuple(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
b=10.3
int(b)
10
complex(b)
(10.3+0j)
str(b)
'10.3'
list(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dic(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dic(b)
NameError: name 'dic' is not defined. Did you mean: 'dir'?
bool(b)
True
c=10+5J
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
list(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
str(c)
'(10+5j)'
tuple(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s="Nagaraju"
int(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'Nagaraju'
list(s)
['N', 'a', 'g', 'a', 'r', 'a', 'j', 'u']
tuple(s)
('N', 'a', 'g', 'a', 'r', 'a', 'j', 'u')
set(s)
{'a', 'N', 'u', 'g', 'r', 'j'}
bool(s)
True
s="12,15,"
int
<class 'int'>
int(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '12,15,'
s='12','14'
int(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
s=('12','14')
int(s)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
k='12'
int(k)
12
float(k)
12.0
complex(k)
(12+0j)
l=[1,2,3,4,6,]
int(l)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
str(l)
'[1, 2, 3, 4, 6]'
tuple(l)
(1, 2, 3, 4, 6)
set(l)
{1, 2, 3, 4, 6}
bool(l)
True
t=(1,2,3,4,5,6)
int(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
list(t)
[1, 2, 3, 4, 5, 6]
set(t)
{1, 2, 3, 4, 5, 6}
bool(t)
True
p={1,2,3,8,9}
int(p)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    int(p)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(p)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    float(p)
TypeError: float() argument must be a string or a real number, not 'set'
complex(p)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    complex(p)
TypeError: complex() argument must be a string or a number, not set
str(p)
'{1, 2, 3, 8, 9}'
list(p)
[1, 2, 3, 8, 9]
tuple(p)
(1, 2, 3, 8, 9)
bool(p)
True
dic(p)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    dic(p)
NameError: name 'dic' is not defined. Did you mean: 'dir'?
d={"Name":"Nagaraju","no":"12"}
int(d)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> str(d)
"{'Name': 'Nagaraju', 'no': '12'}"
>>> list(d)
['Name', 'no']
>>> tuple(d)
('Name', 'no')
>>> set(d)
{'no', 'Name'}
>>> bool(d)
True
>>> b=True
>>> int(b)
1
>>> float(b)
1.0
>>> complex(b)
(1+0j)
>>> str(b)
'True'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
