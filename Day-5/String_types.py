Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='fgfgdag'
s
'fgfgdag'
type(s)
<class 'str'>
s="fadgdag"
s='''gfdagad;'''
s=''
fname='dfaff'
lname='dsf'
fname+lname
'dfaffdsf'

fname*7
'dfaffdfaffdfaffdfaffdfaffdfaffdfaff'
fname*20
'dfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaffdfaff'
s='python'
s[4]
'o'
s[6]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s[6]
IndexError: string index out of range
s[5]
'n'
s[3]
'h'
s[-1]
'n'
s[-5]
'y'
name="nagaraju mahesh srinu"
name=[5]
name[5]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name[5]
IndexError: list index out of range
name
[5]
name="nagaraju mahesh srinu"
name
'nagaraju mahesh srinu'
name[5]
'a'
name[-1]
'u'
name[-15]
'j'
name[0:8]
'nagaraju'
name[9:15]
'mahesh'
name[16:21]
'srinu'
name[-1:-5]
''
name[-1:-8]
''
name[-1:-2:-1]
'u'
name[::2]
'ngrj aehsiu'
name[-1:-5:-1]
'unir'
name[-4:]
'rinu'
name[-5:]
'srinu'
name
'nagaraju mahesh srinu'
name[-6:-11:-1]
' hseh'
name[-7:-13:-1]
'hseham'
name[-13:]
' mahesh srinu'
name
'nagaraju mahesh srinu'
'nagaraju' in name
True
'mahesh' in name
True
'mehooboba' in name
False
name
'nagaraju mahesh srinu'
len(names)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    len(names)
NameError: name 'names' is not defined. Did you mean: 'name'?
len(name)
21
sorted(name)
[' ', ' ', 'a', 'a', 'a', 'a', 'e', 'g', 'h', 'h', 'i', 'j', 'm', 'n', 'n', 'r', 'r', 's', 's', 'u', 'u']
max(name)
'u'
min(name)
' '
ord('a')
97
ord('b')
98
ord('A')
65
ord('O')
79
chr('a')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    chr('a')
TypeError: 'str' object cannot be interpreted as an integer
chr(112)
'p'
chr(118)
'v'
chr(20)
'\x14'
names
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'name'?
name
'nagaraju mahesh srinu'
name.upper
<built-in method upper of str object at 0x0000019C0D609C30>
name.upper()
'NAGARAJU MAHESH SRINU'
name.lower()
'nagaraju mahesh srinu'
name.capitalize()
'Nagaraju mahesh srinu'
name.title()
'Nagaraju Mahesh Srinu'
name.swapcas()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    name.swapcas()
AttributeError: 'str' object has no attribute 'swapcas'. Did you mean: 'swapcase'?
name.swapcase()
'NAGARAJU MAHESH SRINU'
name
'nagaraju mahesh srinu'
name.swapcase()
'NAGARAJU MAHESH SRINU'
name.swapcase()
'NAGARAJU MAHESH SRINU'
name='Nagaraju Mahesh Srinu'
name.swapcase()
'nAGARAJU mAHESH sRINU'
name.casefold()
'nagaraju mahesh srinu'
name='Nagaraju Mahesh Srinu'
name.casefold()
SyntaxError: multiple statements found while compiling a single statement
name
'Nagaraju Mahesh Srinu'
name.center(20,'*')
'Nagaraju Mahesh Srinu'
name.center(50,'*')
'**************Nagaraju Mahesh Srinu***************'
name.cnter(70,' ')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    name.cnter(70,' ')
AttributeError: 'str' object has no attribute 'cnter'. Did you mean: 'center'?
name.center(70,'-')
'------------------------Nagaraju Mahesh Srinu-------------------------'
name.ljust(70,'-')
'Nagaraju Mahesh Srinu-------------------------------------------------'
name.rjust(70,'-')
'-------------------------------------------------Nagaraju Mahesh Srinu'
num='6445522'
num.zfill(10)
'0006445522'
num.zfill(5)
'6445522'
num.zfill(3)
'6445522'

name
'Nagaraju Mahesh Srinu'
namr.find('srinu')
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    namr.find('srinu')
NameError: name 'namr' is not defined. Did you mean: 'name'?
name.find('srinu')
-1
name.find('mahesh')
-1
name
'Nagaraju Mahesh Srinu'
name.find('Srinu')
16
name.find('M)
          
SyntaxError: unterminated string literal (detected at line 1)
name.find('M')
          
9
name.find('z')
          
-1
name.index('a)
           
SyntaxError: unterminated string literal (detected at line 1)
name.index('a')
           
1
name.rfind('a)
           
SyntaxError: unterminated string literal (detected at line 1)
name.rfind('a')
           
10
name.index('a')
           
1
name.index('z')
           
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    name.index('z')
ValueError: substring not found
name.count('a')
           
4
name.count('N')
           
1
name.count('s')
           
1
name
           
'Nagaraju Mahesh Srinu'
name.rplace('a','*')
           
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    name.rplace('a','*')
AttributeError: 'str' object has no attribute 'rplace'. Did you mean: 'replace'?
name.replace('a','*')
           
'N*g*r*ju M*hesh Srinu'
name.replace('
             
SyntaxError: unterminated string literal (detected at line 1)
name.replace('N','k')
             
'kagaraju Mahesh Srinu'
name.replace('priya','Nagaraju')
             
'Nagaraju Mahesh Srinu'
name.maketrans('aeiou','12345')
             
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
name.translate(name.maketrans('aeiou','12345'))
             
'N1g1r1j5 M1h2sh Sr3n5'
name
             
'Nagaraju Mahesh Srinu'
name.split()
             
['Nagaraju', 'Mahesh', 'Srinu']
name.split(' ',2)
             
['Nagaraju', 'Mahesh', 'Srinu']
name.rsplit(' ',1)
             
['Nagaraju Mahesh', 'Srinu']
s='python\nprogramming\nlang'
             
s
             
'python\nprogramming\nlang'
s.splitline()
             
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    s.splitline()
AttributeError: 'str' object has no attribute 'splitline'. Did you mean: 'splitlines'?
s.splitlines()
             
['python', 'programming', 'lang']
l=['python', 'programming', 'lang']
','.joint(1)
             
SyntaxError: multiple statements found while compiling a single statement
l=['python', 'programming', 'lang']

','.join()
             
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    ','.join()
TypeError: str.join() takes exactly one argument (0 given)
','.join(l)
             
'python,programming,lang'
','.join(n)
             
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    ','.join(n)
NameError: name 'n' is not defined
name
             
'Nagaraju Mahesh Srinu'
n=['python', 'programming', 'lang']
'@'.joint(n)
             
SyntaxError: multiple statements found while compiling a single statement
name
             
'Nagaraju Mahesh Srinu'
names.partition(' ')
             
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    names.partition(' ')
NameError: name 'names' is not defined. Did you mean: 'name'?
name.partition(' ')
             
('Nagaraju', ' ', 'Mahesh Srinu')
name.partition('M')
             
('Nagaraju ', 'M', 'ahesh Srinu')
name.rpartition('e')
             
('Nagaraju Mah', 'e', 'sh Srinu')
name.partition('a')
             
('N', 'a', 'garaju Mahesh Srinu')
('N', 'a', 'garaju Mahesh Srinu')
             
('N', 'a', 'garaju Mahesh Srinu')
s='     hellow      world   '
             
s.strip()
             
'hellow      world'
s.lstrip()
             
'hellow      world   '
s.rsrip()
             
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    s.rsrip()
AttributeError: 'str' object has no attribute 'rsrip'. Did you mean: 'rstrip'?
s.rstrip()
             
'     hellow      world'
s.replace(' ','')
             
'hellowworld'
>>> text= 'Nagaraju is good boy'
...              
>>> text.encode()
...              
b'Nagaraju is good boy'
>>> b'Nagaraju is good boy'.decode()
...              
'Nagaraju is good boy'
>>> text='hello  cafe "
...              
SyntaxError: unterminated string literal (detected at line 1)
>>> text="gjfgjdfskgfdskogm"
...              
>>> text.encode()
...              
b'gjfgjdfskgfdskogm'
>>> text="👍"
...              
>>> text.encode()
...              
b'\xf0\x9f\x91\x8d'
>>> b'\xf0\x9f\x91\x8d'.decode()
...              
'👍'
