Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict
>>> d={}
>>> d=dict()
>>> type(D)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(D)
NameError: name 'D' is not defined. Did you mean: 'd'?
>>> type(d)
<class 'dict'>
>>> d={'name':'asif','batch':52,'skills':['python','css','html']}
>>> d['name']='asif'
>>> d
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html']}
>>> d['course']='mehaboob'
>>> d
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'mehaboob'}
>>> s={}
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[1]
KeyError: 1
s
{}
s[1]='int'
s
{1: 'int'}
s[1.2]='float'
s['demo']='string'
s
{1: 'int', 1.2: 'float', 'demo': 'string'}
s['(1,2,3,4,5,6)']='tuple'
s
{1: 'int', 1.2: 'float', 'demo': 'string', '(1,2,3,4,5,6)': 'tuple'}
s[True]='boolen'
s
{1: 'boolen', 1.2: 'float', 'demo': 'string', '(1,2,3,4,5,6)': 'tuple'}
s['True']='boolen'
s
{1: 'boolen', 1.2: 'float', 'demo': 'string', '(1,2,3,4,5,6)': 'tuple', 'True': 'boolen'}
#dic is mutable,not allowed duplicates
s[(1,2,3)]='set'
s
{1: 'boolen', 1.2: 'float', 'demo': 'string', '(1,2,3,4,5,6)': 'tuple', 'True': 'boolen', (1, 2, 3): 'set'}
s[{1:1,2:2}]='dict'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s[{1:1,2:2}]='dict'
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
a={}
a={1:1}
a
{1: 1}
"nagaraju" in d
False
'mehaboob' in d
False
s
{1: 'boolen', 1.2: 'float', 'demo': 'string', '(1,2,3,4,5,6)': 'tuple', 'True': 'boolen', (1, 2, 3): 'set'}
d
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'mehaboob'}
d['name']
'asif'
d['skills']
['python', 'css', 'html']
d['course']
'mehaboob'
d['age']
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d['age']
KeyError: 'age'
d.get('age')
d.get('course')
'mehaboob'
d.get('age','age is not present')
'age is not present'
d.get('name','name is not present')
'asif'
d
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'mehaboob'}
d['course']='PFS'
d
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS'}
d['age']=21
d
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21}
d['dfgdf]='adgadg'
  
SyntaxError: unterminated string literal (detected at line 1)
d['gdfaga']='gfadgg'
  
d
  
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg'}
d.update({'fdsaf':'fadfsd','k3':'gdgda'})
  
d
  
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd', 'k3': 'gdgda'}
d.popitem()
  
('k3', 'gdgda')
d
  
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd'}
d.pop('name')
  
'asif'
d
  
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd'}
del d['batch'}
  
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
del d['batch']
  
d
  
{'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd'}
d.clear()
  
d
  
{}
d={'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd'}
  
d
  
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd'}
d.key()
  
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
d.keys()
  
dict_keys(['batch', 'skills', 'course', 'age', 'gdfaga', 'fdsaf'])
d.values()
  
dict_values([52, ['python', 'css', 'html'], 'PFS', 21, 'gfadgg', 'fadfsd'])
d.items()
  
dict_items([('batch', 52), ('skills', ['python', 'css', 'html']), ('course', 'PFS'), ('age', 21), ('gdfaga', 'gfadgg'), ('fdsaf', 'fadfsd')])
sorted(d)
  
['age', 'batch', 'course', 'fdsaf', 'gdfaga', 'skills']
len(d)
  
6
max(d)
  
'skills'
min(d)
  
'age'
d
  
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd'}
d.get('name')
  
d
  
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd'}
d.setdefault('name','')
  
''
d
  
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd', 'name': ''}
d.get('get')
  
d.get('age')
  
21
d.setdefault('age',24)
  
21
d
  
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'gdfaga': 'gfadgg', 'fdsaf': 'fadfsd', 'name': ''}
