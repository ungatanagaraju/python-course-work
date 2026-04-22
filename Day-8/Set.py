Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
                     #set
#Mutable
#dyanmic
#no duplicates
#unorder
#Membership operator is faster
#it is hetrogenus
s=set()
s={1,2,3,4,1,2,2,3,5}
s
{1, 2, 3, 4, 5}
s.add(100)
s
{1, 2, 3, 4, 5, 100}
s.add(0)
s
{0, 1, 2, 3, 4, 5, 100}
s.add(30)
s
{0, 1, 2, 3, 4, 5, 100, 30}
{0, 1, 2, 3, 4, 5, 100, 30}
{0, 1, 2, 3, 4, 5, 100, 30}
s.add(10.2)
s
{0, 1, 2, 3, 4, 5, 10.2, 30, 100}
s.add('string')
s
{0, 1, 2, 3, 4, 5, 10.2, 'string', 30, 100}
s.add([1,2])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.add([1,2])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s
{0, 1, 2, 3, 4, 5, 10.2, 'string', 30, 100}
1 in s
True
2 not in s
False
for i in s
SyntaxError: expected ':'
for i in s:
    print(i)

    
0
1
2
3
4
5
10.2
string
30
100
a={9,8,7,1,2,3}
b={5,3,4,1,2,7}
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a.union(b)
{1, 2, 3, 4, 5, 7, 8, 9}
a|b
{1, 2, 3, 4, 5, 7, 8, 9}
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a.intersection(b)
{1, 2, 3, 7}
a
{1, 2, 3, 7, 8, 9}
a
{1, 2, 3, 7, 8, 9}
a
{1, 2, 3, 7, 8, 9}
a&b
{1, 2, 3, 7}
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a-b
{8, 9}
\
a
{1, 2, 3, 7, 8, 9}
{1}<a
True
{9,10}<a
False
a>{1}
True
a>{1,2,3,4,5}
False
a>{1,2,8,9}
True
a
{1, 2, 3, 7, 8, 9}
a.isdisjoint(C)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.isdisjoint(C)
NameError: name 'C' is not defined
a.isdisjoint(c)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.isdisjoint(c)
NameError: name 'c' is not defined
a
{1, 2, 3, 7, 8, 9}
b={10,11}
b
{10, 11}
a.isdisjoint(c)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.isdisjoint(c)
NameError: name 'c' is not defined
#adding
a.add(100)
a
{1, 2, 3, 100, 7, 8, 9}
a.add(50)
a
{1, 2, 3, 100, 50, 7, 8, 9}
a.update(70)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.update(70)
TypeError: 'int' object is not iterable
a.update({70,80,90})
a
{1, 2, 3, 100, 70, 7, 8, 9, 80, 50, 90}
a.remove(70)
a
{1, 2, 3, 100, 7, 8, 9, 80, 50, 90}
a.remove(70)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.remove(70)
KeyError: 70
a
{1, 2, 3, 100, 7, 8, 9, 80, 50, 90}
a.remove(7)
a
{1, 2, 3, 100, 8, 9, 80, 50, 90}
a.discard(7)
a
{1, 2, 3, 100, 8, 9, 80, 50, 90}
{1, 2, 3, 100, 8, 9, 80, 50, 90}
{1, 2, 3, 100, 8, 9, 80, 50, 90}
a
{1, 2, 3, 100, 8, 9, 80, 50, 90}
b
{10, 11}

a={1, 2, 3, 100, 8, 9, 80, 50, 90}
b={1, 2, 3,4, 8, 9,10, 50, 90}
SyntaxError: multiple statements found while compiling a single statement
a
{1, 2, 3, 100, 8, 9, 80, 50, 90}
b
{10, 11}
a.intersection(b)
set()
a={1,2,3,4,5,6,7,8}
b={20,90,50,8,9.92}
a
{1, 2, 3, 4, 5, 6, 7, 8}
b
{50, 20, 8, 9.92, 90}
a.intersection(b)
{8}
a
{1, 2, 3, 4, 5, 6, 7, 8}
b
{50, 20, 8, 9.92, 90}
a.intersection_updated(b)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.intersection_updated(b)
AttributeError: 'set' object has no attribute 'intersection_updated'. Did you mean: 'intersection_update'?
b
{50, 20, 8, 9.92, 90}
c=b
c.add(10)
c
{50, 10, 20, 8, 9.92, 90}
b
{50, 10, 20, 8, 9.92, 90}
e=c.copy()
e
{50, 10, 20, 8, 9.92, 90}
>>> e.add(1000)
>>> e
{50, 10, 20, 8, 9.92, 90, 1000}
>>> c
{50, 10, 20, 8, 9.92, 90}
>>> len(c)
6
>>> max(c)
90
>>> min(c)
8
>>> sorted(c)
[8, 9.92, 10, 20, 50, 90]
>>> sum(c)
187.92000000000002
>>> frozen=frozenset([1,2,3})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> frozen=frozenset([1,2,3])
>>> frozen.add(10)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    frozen.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
