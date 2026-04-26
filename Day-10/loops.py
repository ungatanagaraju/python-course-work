Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#str,list,tuple,set,dict,range()
s='python'
for i in s:
    print(i)

    
p
y
t
h
o
n
l=[1,2,3,4]
for i in l:
    print(i)

    
1
2
3
4
t={2,3,4,5}
for i in t:
    print(i)

    
2
3
4
5
f={1,2,3,4}
for i in f:
    print(i)

    
1
2
3
4
\
d={1:1,2:2,3:3,4:4}
for i in d:
    print(i,d[i])

    
1 1
2 2
3 3
4 4
4 4
SyntaxError: invalid syntax
# Range
for i in range(0,10,1)
SyntaxError: expected ':'
for i in range(0,10,1):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i in range(10,0,2)
SyntaxError: expected ':'
for i in range(10,0,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
for i in range(5,50,5)
SyntaxError: expected ':'
for i in range(5,50,5):
    print(i)

    
5
10
15
20
25
30
35
40
45

for i in range(30,40):
    print(i)

    
30
31
32
33
34
35
36
37
38
39

 
for i in enumerate(s):
    print(i)

    
(0, 'p')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')
for i in range(len(s)):
    print(i)

    
0
1
2
3
4
5
for i in range(s)
SyntaxError: expected ':'
for i in range(s):
    print(i,s[i])

    
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    for i in range(s):
TypeError: 'str' object cannot be interpreted as an integer
for i in range(len(s)):
    print(i,s[i])

    
0 p
1 y
2 t
3 h
4 o
5 n
for i in range(len(s)):
    print(i[0])

    
Traceback (most recent call last):
  File "<pyshell#58>", line 2, in <module>
    print(i[0])
TypeError: 'int' object is not subscriptable
for i in enumerate(s):
    print(i[0])

    
0
1
2
3
4
5
names = ['Nagaraju','abhairam','saikiran']
for i in enumerate(names):
    print(i[0],i[1])

    
0 Nagaraju
1 abhairam
2 saikiran
for i in range(len(names)):
    print(i,names[i])

    
0 Nagaraju
1 abhairam
2 saikiran
for i in enumerate(names[0]):
    print(i[0],i[1])

    
0 N
1 a
2 g
3 a
4 r
5 a
6 j
7 u

for i in enumerate(names[0]):
    print(i)

    
(0, 'N')
(1, 'a')
(2, 'g')
(3, 'a')
(4, 'r')
(5, 'a')
(6, 'j')
(7, 'u')
>>> s={1,2,3}
>>> for i in enumerate(d)
SyntaxError: expected ':'
>>> for i in enumerate(d):
...     print(i)
... 
...     
(0, 1)
(1, 2)
(2, 3)
(3, 4)
>>> for i in range(len(s)):
...     print(i[0])
... 
...     
Traceback (most recent call last):
  File "<pyshell#80>", line 2, in <module>
    print(i[0])
TypeError: 'int' object is not subscriptable
>>> d={1:1,2:4,3:9,4:16}
>>> for i in enumerate(d)
SyntaxError: expected ':'
>>> for i in enumerate(d):
...     print(i)

    
(0, 1)
(1, 2)
(2, 3)
(3, 4)
for i in enumerate(d):
    print(i[0],i[1],d[i[1])
          
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

          
0 1 1
1 2 4
2 3 9
3 4 16
#brak, continus , pass
          
#brak, continus , pass
          
for i in range(10)]
    
SyntaxError: unmatched ']'
for i in range(10):
    pass

for i in range(10):
    if i==6:
        break
    print(i)

    
0
1
2
3
4
5
for i in range(10):
    if i==8:
        continue
    print(i)

    
0
1
2
3
4
5
6
7
9
#for with else
 pin=12345
 
SyntaxError: unexpected indent
pin=12345

for i in range(5):
    epin=int(input("Enter the pin:"))
    if pin==epin:
        print("Login successful")
        break
    else:
        print("Incorrect pin")
else:
    print("Try Again after 60 Seconds")

    
Enter the pin:12345
Login successful





