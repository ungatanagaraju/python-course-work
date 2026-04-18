Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
nagaraju
name
'nagaraju'
type(name)
<class 'str'>
name = input("Enter the name:")
Enter the name: nagaraju
Enter the name: nagaraju
SyntaxError: invalid syntax
name
' nagaraju'
age=input()
10
age
'10'
age=int(input("Enter the interger:"))
Enter the interger:12
age
12
price= float(input("Enter the float:"))
Enter the float:12.3
Price
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Price
NameError: name 'Price' is not defined. Did you mean: 'price'?
price= float(input("Enter the float:"))
Enter the float:dgsfgsdg
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    price= float(input("Enter the float:"))
ValueError: could not convert string to float: 'dgsfgsdg'
'sfgfgfd,gdfgdg,dsfgdfsg'.split('')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    'sfgfgfd,gdfgdg,dsfgdfsg'.split('')
ValueError: empty separator
'sfgfgfd,gdfgdg,dsfgdfsg'.split(' ')
['sfgfgfd,gdfgdg,dsfgdfsg']
'12
SyntaxError: unterminated string literal (detected at line 1)
'1 2 3 4 5 6 '.split()
['1', '2', '3', '4', '5', '6']
'java,python,html'.split(','java,python,html')
                         
SyntaxError: unterminated string literal (detected at line 1)
'java,python,html'.split(','java python html')
                         
SyntaxError: unterminated string literal (detected at line 1)
'java,python,html'.split(',java,python,html')
                         
['java,python,html']
'java,python,html'.split(',')
                         
['java', 'python', 'html']
lang =input("Enter the lang: ")
                         
Enter the lang:  java html css python
lang
                         
' java html css python'
name=input("Enter the names:").split(',')
                         
Enter the names: nagaraju, raju
name
                         
[' nagaraju', ' raju']
numbers=input("Enter the numbers").split()
                         
Enter the numbers1 2 3 3
numbers
                         
['1', '2', '3', '3']
int(['1', '2', '3', '3'])
                         
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int(['1', '2', '3', '3'])
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
map(int,['1', '2', '3', '3'])
                         
<map object at 0x000002BBD0777840>
list(map(int,['1', '2', '3', '3']))
                         
[1, 2, 3, 3]
number=list(map(int,input("Enter the nums:").split()))
                         
Enter the nums: 4  5  66 888 999
numbers
                         
['1', '2', '3', '3']
numbers
                         
['1', '2', '3', '3']
number=list(map(int,input("Enter the nums:").split()))
                         
Enter the nums:4 6 8  10 55 66 88 8956
numbers
                         
['1', '2', '3', '3']
number
                         
[4, 6, 8, 10, 55, 66, 88, 8956]
numbers = tuple(map(int,input("Enter the nums:").split()))
                         
Enter the nums: 1 2
numbers
                         
(1, 2)
numbers = tuple(map(float,input("Enter the nums:").split()))
                         
Enter the nums:12.5 45.6
numbers
                         
(12.5, 45.6)
names = tuples(input().split())
                         
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    names = tuples(input().split())
NameError: name 'tuples' is not defined. Did you mean: 'tuple'?
names = tuple(input().split())
                         

names = tuple(input().split())
                         
aafa fadsgfdsa afaf
names
                         
('aafa', 'fadsgfdsa', 'afaf')
name = set(input().split())
                         
adfff  adfads afdfasdf
names
                         
('aafa', 'fadsgfdsa', 'afaf')
numbers=set(float,input("Enter the nums:").split()))
                         
SyntaxError: unmatched ')'
numbers=set(float,input("Enter the nums:").split())
                         
Enter the nums:5468 4586
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    numbers=set(float,input("Enter the nums:").split())
TypeError: set expected at most 1 argument, got 2
numbers
                         
(12.5, 45.6)
numbers= set(map(float,input("Enter the nums:").split()))
                         
Enter the nums:4556 45522 
number
                         
[4, 6, 8, 10, 55, 66, 88, 8956]
a,b,c=list(map(int,input().split()))
                         
1 2 3
a
                         
1
b
                         
2
c
                         
3
email,password = ['@gmail.com','pass@123]
                  
SyntaxError: unterminated string literal (detected at line 1)

email,password = ['@gmail.com','pass@123']
                  
email,password= input().split()
                  
nagaraju@codegnan.com@123
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    email,password= input().split()
ValueError: not enough values to unpack (expected 2, got 1)
email
                  
'@gmail.com'
a
                  
1
a=eval(input())
                  
12
a
                  
12
a=eval(input())
                  
34568.5642
a
                  
34568.5642
a=eval(input("Enter the input:"))
                  
Enter the input:'safaffads'
a
                  
'safaffads'
a=eval(input("Enter the input:"))
                  
Enter the input:[1,1,1,2,3]
a
                  
[1, 1, 1, 2, 3]
a=eval(input(Enter the input:"))
             
SyntaxError: unterminated string literal (detected at line 1)
a=eval(input("Enter the input:"))
             
Enter the input:(1,2,3)
a
             
(1, 2, 3)
a=eval(input("Enter the input:"))
             
Enter the input:{1,2,3,4}
a
             
{1, 2, 3, 4}
a=eval(input("Enter the input:"))
             
Enter the input:{1:2,2;3,3:4}
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a=eval(input("Enter the input:"))
  File "<string>", line 1
    {1:2,2;3,3:4}
         ^
SyntaxError: ':' expected after dictionary key
Enter the input:{1:2,2:3,3:4}
             
SyntaxError: invalid syntax
Enter the input:{1:2,2:3,3:4}
             
SyntaxError: invalid syntax
a=eval(input("Enter the input:"))
             
Enter the input:True
a
             
True
a,b,c=10,10.3,'python'
             
a
             
10
b
             
10.3
c
             
'python'
print(a,b,c)
             
10 10.3 python
print("a =",a,"b =",b,"c =",c)
             
a = 10 b = 10.3 c = python
print("a =",a,"b =",b,"c =",c,sep='')
             
a =10b =10.3c =python
KeyboardInterrupt
print("a =",a,"b =",b,"c =",c,sep=\n')
      
SyntaxError: unexpected character after line continuation character
print("a =",a,"b =",b,"c =",c,sep'')
      
SyntaxError: invalid syntax
print("a =",a,"b =",b,"c =",c,sep='')
      
a =10b =10.3c =python
print("a =",a,"b =",b,"c =",c,sep='\n')
      
a =
10
b =
10.3
c =
python
print("a =",a,"b =",b,"c =",c,sep='@@@')
      
a =@@@10@@@b =@@@10.3@@@c =@@@python
print("a =",a,"b =",b,"c =",c,sep='@@@',end='\n\n')
      
a =@@@10@@@b =@@@10.3@@@c =@@@python

>>> print("a =",a,"b =",b,"c =",c,sep='@@@'end='.........')
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("a =",a,"b =",b,"c =",c,sep='@@@',end='.......')
...       
a =@@@10@@@b =@@@10.3@@@c =@@@python.......
>>> print(f'a={a} b={b} c{c}')
...       
a=10 b=10.3 cpython
>>> print('a=%d b=%f c=%s'%(a,b,c))
...       
a=10 b=10.300000 c=python
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
...       
a=10 b=10.30 c=python
>>> print('a={} b={} c={}'.format(a,b,c))
...       
a=10 b=10.3 c=python
>>> a=10 b=10.3 c=python
...       
SyntaxError: invalid syntax
>>> print('a={2} b={0} c={1}'.format(a,b,c))
...       
a=python b=10 c=10.3
