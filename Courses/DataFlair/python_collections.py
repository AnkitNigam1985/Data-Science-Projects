<<<<<<< HEAD
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import Counter,defaultdict,OrderedDict,namedtuple
>>> 
>>> issubclass(Counter,dict) and issubclass(defaultdict,dict) and issubclass(OrderedDict,dict)
True
>>> 
>>> 
>>> type(namedtuple)
<class 'function'>
>>> 
>>> 
>>> type(Counter)
<class 'type'>
>>> 
>>> 
>>> type(defaultdict)
<class 'type'>
>>> 
>>> type(OrderedDict)
<class 'type'>
>>> 
>>> 
>>> 
>>> #Python collections counter
>>> 
>>> from collections import Counter
>>> c=Counter({'a':3,'b':2,'c':1})
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> c=Counter('Hello')
>>> c
Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
>>> 
>>> 
>>> 
>>> c=Counter()
>>> c.update('bfg')
>>> c
Counter({'b': 1, 'f': 1, 'g': 1})
>>> 
>>> 
>>> 
>>> c['f']
1
>>> 
>>> 
>>> for i in c.elements():
	print(i)

	
b
f
g
>>> for i in c.elements():
	print(i, c[i])

	
b 1
f 1
g 1
>>> c.most_common(2)
[('b', 1), ('f', 1)]
>>> 
>>> c=Counter('hello')
>>> c
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
>>> c.most_common(2)
[('l', 2), ('h', 1)]
>>> c.most_common(1)
[('l', 2)]
>>> 
>>> 
>>> 
>>> 
>>> #Python Default Dict
>>> 
>>> 
>>> from collections import defaultdict
>>> 
>>> 
>>> d=defaultdict(lambda :35)
>>> 
>>> d
defaultdict(<function <lambda> at 0x02B2AC40>, {})
>>> d['Ayushi']=95
>>> d['Bree']=89
>>> d['Leo']=90.5
>>> d['Adam']
35
>>> 
>>> d
defaultdict(<function <lambda> at 0x02B2AC40>, {'Ayushi': 95, 'Bree': 89, 'Leo': 90.5, 'Adam': 35})
>>> d['Ankit']
35
>>> d
defaultdict(<function <lambda> at 0x02B2AC40>, {'Ayushi': 95, 'Bree': 89, 'Leo': 90.5, 'Adam': 35, 'Ankit': 35})
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> d=defaultdict(list)
>>> d
defaultdict(<class 'list'>, {})
>>> for i,j in [('a',(1,2)),('b',(3,4)),('c',(5,6))]:
	d[i].append(j)

	
>>> d
defaultdict(<class 'list'>, {'a': [(1, 2)], 'b': [(3, 4)], 'c': [(5, 6)]})
>>> 
>>> 
>>> 
>>> #Python OrderedDict
>>> 
>>> 
>>> o=OrderedDict()
>>> o['a']=3
>>> o['c']=1
>>> o['b']=4
>>> o
OrderedDict([('a', 3), ('c', 1), ('b', 4)])
>>> 
>>> 
>>> o.move_to_end('c')
>>> o
OrderedDict([('a', 3), ('b', 4), ('c', 1)])
>>> o.popitem()
('c', 1)
>>> o
OrderedDict([('a', 3), ('b', 4)])
>>> 
>>> 
>>> 
>>> 
>>> #Python NamedTuple
>>> 
>>> from collections import namedtuple
>>> 
>>> colors=namedtuple('colors','r g b')
>>> 
>>> red=colors(r=255,g=0,b=0)
>>> 
>>> 
>>> red
colors(r=255, g=0, b=0)
>>> colors
<class '__main__.colors'>
>>> red.r
255
>>> red.g
0
>>> red.b
0
>>> red.as_dict()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    red.as_dict()
AttributeError: 'colors' object has no attribute 'as_dict'
>>> red._asdict()
{'r': 255, 'g': 0, 'b': 0}
>>> 
>>> 
>>> red
colors(r=255, g=0, b=0)
>>> x=red._asdict()
>>> x
{'r': 255, 'g': 0, 'b': 0}
>>> 
>>> 
>>> colors._make(['1','2','3'])
colors(r='1', g='2', b='3')
>>> 
>>> 
>>> 
>>> 
>>> #Python counter revisited
>>> 
>>> c=Counter(['a','b','c','a','b','a'])
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> issubclass(Counter,dict)
True
>>> 
>>> 
>>> c=Counter(['a','b','c','a','b','a'])
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> 
>>> 
>>> 
>>> c=Counter(('a','b','c','a','b','a'))
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> 
>>> 
>>> c=Counter("Hello")
>>> c
Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
>>> 
>>> 
>>> c=Counter({'a':3,'b':2,'c':1})
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> 
>>> 
>>> 
>>> c=Counter(a=3,b=2,c=1)
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> 
>>> 
>>> d=Counter()
>>> d.update("Hello")
>>> d
Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
>>> d['e']
1
>>> 
>>> 
>>> e=Counter("Hello")
>>> for i in "Help":
	print(f"{i}: {e[i]}")

	
H: 1
e: 1
l: 2
p: 0
>>> e=Counter({'a':3,'b':2,'c':1,'d':0})
>>> 
>>> for i in e.elements():
	print(f"{i}: {e[i]}")

	
a: 3
a: 3
a: 3
b: 2
b: 2
c: 1
>>> 
>>> 
>>> e.most_common(2)
[('a', 3), ('b', 2)]
>>> 
>>> e['e']=5
>>> 
>>> e
Counter({'e': 5, 'a': 3, 'b': 2, 'c': 1, 'd': 0})
>>> 
>>> 
>>> e.clear()
>>> 
>>> 
>>> e
Counter()
>>> 
>>> 
>>> a=Counter({'a':3,'b':2,'c':1})
>>> b=Counter({'c':3,'d':2,'e':1})
>>> 
>>> a+b
Counter({'c': 4, 'a': 3, 'b': 2, 'd': 2, 'e': 1})
>>> 
>>> 
>>> 
>>> 
>>> #Python NamedTuple revisited
>>> 
>>> 
>>> 
>>> colors=(255,0,0)
>>> 
>>> colors[0]
255
>>> 
>>> colors[1]=10
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    colors[1]=10
TypeError: 'tuple' object does not support item assignment
>>> 
>>> Colors=namedtuple('Colors','red green blue')
>>> Colors
<class '__main__.Colors'>
>>> 
>>> type(namedtuple)
<class 'function'>
>>> 
>>> red=Colors(red=255,green=0,blue=0)
>>> green=Colors(red=0,green=255,blue=0)
>>> blue=Colors(red=0,green=0,blue=255)
>>> 
>>> red
Colors(red=255, green=0, blue=0)
>>> green
Colors(red=0, green=255, blue=0)
>>> blue
Colors(red=0, green=0, blue=255)
>>> 
>>> 
>>> red.r
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    red.r
AttributeError: 'Colors' object has no attribute 'r'
>>> red.red
255
>>> gree.blue
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    gree.blue
NameError: name 'gree' is not defined
>>> 
>>> green.blue
0
>>> 
>>> 
>>> 
>>> 
>>> pets=namedtuple('pets',['name','age'])
>>> 
>>> pets
<class '__main__.pets'>
>>> Fluffy=pets('Fluffy',8)
>>> 
>>> Fluffy
pets(name='Fluffy', age=8)
>>> 
>>> Fluffy.name
'Fluffy'
>>> Fluffy.age
8
>>> 
>>> 
>>> 
>>> 
>>> #Python DefaultDict revisited
>>> 
>>> issubclass(defaultdict,dict)
True
>>> 
>>> mydict={'a':1,'b':2,'c':3}
>>> mydict['b']
2
>>> 
>>> otherdict=dict((['a',1],['b',2],['c',3]))
>>> otherdict
{'a': 1, 'b': 2, 'c': 3}
>>> 
>>> otherdict['d']
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    otherdict['d']
KeyError: 'd'
>>> 
>>> 
>>> 
>>> otherdict=defaultdict(defaultvalue)
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    otherdict=defaultdict(defaultvalue)
NameError: name 'defaultvalue' is not defined
>>> 
>>> 
>>> def defaultvalue():
	return 0

>>> otherdict=defaultdict(defaultvalue)
>>> 
>>> otherdict['a']=1
>>> otherdict['b']=2
>>> 
>>> otherdict['c']
0
>>> 
>>> otherdict
defaultdict(<function defaultvalue at 0x02C236A0>, {'a': 1, 'b': 2, 'c': 0})
>>> 
>>> 
>>> 
>>> 
>>> marks=defaultdict(lambda :35)
>>> marks['Ayushi']=95
>>> marks['Gigi']=86
>>> marks['Ayushi']
95
>>> 
>>> marks
defaultdict(<function <lambda> at 0x02C236E8>, {'Ayushi': 95, 'Gigi': 86})
>>> 
>>> 
>>> 
>>> 
>>> #Python Ordered Dict revisited
>>> 
>>> d=OrderedDict()
>>> 
>>> 
>>> d['a']=1
>>> d['e']=5
>>> d['d']=4
>>> d['b']=2
>>> d['c']=3
>>> 
>>> d
OrderedDict([('a', 1), ('e', 5), ('d', 4), ('b', 2), ('c', 3)])
>>> d.move_to_end('e')
>>> d
OrderedDict([('a', 1), ('d', 4), ('b', 2), ('c', 3), ('e', 5)])
>>> d.pop('e')
5
>>> d
OrderedDict([('a', 1), ('d', 4), ('b', 2), ('c', 3)])
>>> 
>>> 
>>> 
>>> 
>>> g=OrderedDict()
>>> g['d']=4
>>> g['b']=2
>>> g['a']=1
>>> g['c']=3
>>> g['e']=5
>>> g
OrderedDict([('d', 4), ('b', 2), ('a', 1), ('c', 3), ('e', 5)])
>>> 
>>> 
>>> g.popitem(last=False)
('d', 4)
>>> g
OrderedDict([('b', 2), ('a', 1), ('c', 3), ('e', 5)])
>>> g.popitem(last=True)
('e', 5)
>>> g
OrderedDict([('b', 2), ('a', 1), ('c', 3)])
=======
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import Counter,defaultdict,OrderedDict,namedtuple
>>> 
>>> issubclass(Counter,dict) and issubclass(defaultdict,dict) and issubclass(OrderedDict,dict)
True
>>> 
>>> 
>>> type(namedtuple)
<class 'function'>
>>> 
>>> 
>>> type(Counter)
<class 'type'>
>>> 
>>> 
>>> type(defaultdict)
<class 'type'>
>>> 
>>> type(OrderedDict)
<class 'type'>
>>> 
>>> 
>>> 
>>> #Python collections counter
>>> 
>>> from collections import Counter
>>> c=Counter({'a':3,'b':2,'c':1})
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> c=Counter('Hello')
>>> c
Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
>>> 
>>> 
>>> 
>>> c=Counter()
>>> c.update('bfg')
>>> c
Counter({'b': 1, 'f': 1, 'g': 1})
>>> 
>>> 
>>> 
>>> c['f']
1
>>> 
>>> 
>>> for i in c.elements():
	print(i)

	
b
f
g
>>> for i in c.elements():
	print(i, c[i])

	
b 1
f 1
g 1
>>> c.most_common(2)
[('b', 1), ('f', 1)]
>>> 
>>> c=Counter('hello')
>>> c
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
>>> c.most_common(2)
[('l', 2), ('h', 1)]
>>> c.most_common(1)
[('l', 2)]
>>> 
>>> 
>>> 
>>> 
>>> #Python Default Dict
>>> 
>>> 
>>> from collections import defaultdict
>>> 
>>> 
>>> d=defaultdict(lambda :35)
>>> 
>>> d
defaultdict(<function <lambda> at 0x02B2AC40>, {})
>>> d['Ayushi']=95
>>> d['Bree']=89
>>> d['Leo']=90.5
>>> d['Adam']
35
>>> 
>>> d
defaultdict(<function <lambda> at 0x02B2AC40>, {'Ayushi': 95, 'Bree': 89, 'Leo': 90.5, 'Adam': 35})
>>> d['Ankit']
35
>>> d
defaultdict(<function <lambda> at 0x02B2AC40>, {'Ayushi': 95, 'Bree': 89, 'Leo': 90.5, 'Adam': 35, 'Ankit': 35})
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> d=defaultdict(list)
>>> d
defaultdict(<class 'list'>, {})
>>> for i,j in [('a',(1,2)),('b',(3,4)),('c',(5,6))]:
	d[i].append(j)

	
>>> d
defaultdict(<class 'list'>, {'a': [(1, 2)], 'b': [(3, 4)], 'c': [(5, 6)]})
>>> 
>>> 
>>> 
>>> #Python OrderedDict
>>> 
>>> 
>>> o=OrderedDict()
>>> o['a']=3
>>> o['c']=1
>>> o['b']=4
>>> o
OrderedDict([('a', 3), ('c', 1), ('b', 4)])
>>> 
>>> 
>>> o.move_to_end('c')
>>> o
OrderedDict([('a', 3), ('b', 4), ('c', 1)])
>>> o.popitem()
('c', 1)
>>> o
OrderedDict([('a', 3), ('b', 4)])
>>> 
>>> 
>>> 
>>> 
>>> #Python NamedTuple
>>> 
>>> from collections import namedtuple
>>> 
>>> colors=namedtuple('colors','r g b')
>>> 
>>> red=colors(r=255,g=0,b=0)
>>> 
>>> 
>>> red
colors(r=255, g=0, b=0)
>>> colors
<class '__main__.colors'>
>>> red.r
255
>>> red.g
0
>>> red.b
0
>>> red.as_dict()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    red.as_dict()
AttributeError: 'colors' object has no attribute 'as_dict'
>>> red._asdict()
{'r': 255, 'g': 0, 'b': 0}
>>> 
>>> 
>>> red
colors(r=255, g=0, b=0)
>>> x=red._asdict()
>>> x
{'r': 255, 'g': 0, 'b': 0}
>>> 
>>> 
>>> colors._make(['1','2','3'])
colors(r='1', g='2', b='3')
>>> 
>>> 
>>> 
>>> 
>>> #Python counter revisited
>>> 
>>> c=Counter(['a','b','c','a','b','a'])
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> issubclass(Counter,dict)
True
>>> 
>>> 
>>> c=Counter(['a','b','c','a','b','a'])
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> 
>>> 
>>> 
>>> c=Counter(('a','b','c','a','b','a'))
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> 
>>> 
>>> c=Counter("Hello")
>>> c
Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
>>> 
>>> 
>>> c=Counter({'a':3,'b':2,'c':1})
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> 
>>> 
>>> 
>>> c=Counter(a=3,b=2,c=1)
>>> c
Counter({'a': 3, 'b': 2, 'c': 1})
>>> 
>>> 
>>> d=Counter()
>>> d.update("Hello")
>>> d
Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
>>> d['e']
1
>>> 
>>> 
>>> e=Counter("Hello")
>>> for i in "Help":
	print(f"{i}: {e[i]}")

	
H: 1
e: 1
l: 2
p: 0
>>> e=Counter({'a':3,'b':2,'c':1,'d':0})
>>> 
>>> for i in e.elements():
	print(f"{i}: {e[i]}")

	
a: 3
a: 3
a: 3
b: 2
b: 2
c: 1
>>> 
>>> 
>>> e.most_common(2)
[('a', 3), ('b', 2)]
>>> 
>>> e['e']=5
>>> 
>>> e
Counter({'e': 5, 'a': 3, 'b': 2, 'c': 1, 'd': 0})
>>> 
>>> 
>>> e.clear()
>>> 
>>> 
>>> e
Counter()
>>> 
>>> 
>>> a=Counter({'a':3,'b':2,'c':1})
>>> b=Counter({'c':3,'d':2,'e':1})
>>> 
>>> a+b
Counter({'c': 4, 'a': 3, 'b': 2, 'd': 2, 'e': 1})
>>> 
>>> 
>>> 
>>> 
>>> #Python NamedTuple revisited
>>> 
>>> 
>>> 
>>> colors=(255,0,0)
>>> 
>>> colors[0]
255
>>> 
>>> colors[1]=10
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    colors[1]=10
TypeError: 'tuple' object does not support item assignment
>>> 
>>> Colors=namedtuple('Colors','red green blue')
>>> Colors
<class '__main__.Colors'>
>>> 
>>> type(namedtuple)
<class 'function'>
>>> 
>>> red=Colors(red=255,green=0,blue=0)
>>> green=Colors(red=0,green=255,blue=0)
>>> blue=Colors(red=0,green=0,blue=255)
>>> 
>>> red
Colors(red=255, green=0, blue=0)
>>> green
Colors(red=0, green=255, blue=0)
>>> blue
Colors(red=0, green=0, blue=255)
>>> 
>>> 
>>> red.r
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    red.r
AttributeError: 'Colors' object has no attribute 'r'
>>> red.red
255
>>> gree.blue
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    gree.blue
NameError: name 'gree' is not defined
>>> 
>>> green.blue
0
>>> 
>>> 
>>> 
>>> 
>>> pets=namedtuple('pets',['name','age'])
>>> 
>>> pets
<class '__main__.pets'>
>>> Fluffy=pets('Fluffy',8)
>>> 
>>> Fluffy
pets(name='Fluffy', age=8)
>>> 
>>> Fluffy.name
'Fluffy'
>>> Fluffy.age
8
>>> 
>>> 
>>> 
>>> 
>>> #Python DefaultDict revisited
>>> 
>>> issubclass(defaultdict,dict)
True
>>> 
>>> mydict={'a':1,'b':2,'c':3}
>>> mydict['b']
2
>>> 
>>> otherdict=dict((['a',1],['b',2],['c',3]))
>>> otherdict
{'a': 1, 'b': 2, 'c': 3}
>>> 
>>> otherdict['d']
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    otherdict['d']
KeyError: 'd'
>>> 
>>> 
>>> 
>>> otherdict=defaultdict(defaultvalue)
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    otherdict=defaultdict(defaultvalue)
NameError: name 'defaultvalue' is not defined
>>> 
>>> 
>>> def defaultvalue():
	return 0

>>> otherdict=defaultdict(defaultvalue)
>>> 
>>> otherdict['a']=1
>>> otherdict['b']=2
>>> 
>>> otherdict['c']
0
>>> 
>>> otherdict
defaultdict(<function defaultvalue at 0x02C236A0>, {'a': 1, 'b': 2, 'c': 0})
>>> 
>>> 
>>> 
>>> 
>>> marks=defaultdict(lambda :35)
>>> marks['Ayushi']=95
>>> marks['Gigi']=86
>>> marks['Ayushi']
95
>>> 
>>> marks
defaultdict(<function <lambda> at 0x02C236E8>, {'Ayushi': 95, 'Gigi': 86})
>>> 
>>> 
>>> 
>>> 
>>> #Python Ordered Dict revisited
>>> 
>>> d=OrderedDict()
>>> 
>>> 
>>> d['a']=1
>>> d['e']=5
>>> d['d']=4
>>> d['b']=2
>>> d['c']=3
>>> 
>>> d
OrderedDict([('a', 1), ('e', 5), ('d', 4), ('b', 2), ('c', 3)])
>>> d.move_to_end('e')
>>> d
OrderedDict([('a', 1), ('d', 4), ('b', 2), ('c', 3), ('e', 5)])
>>> d.pop('e')
5
>>> d
OrderedDict([('a', 1), ('d', 4), ('b', 2), ('c', 3)])
>>> 
>>> 
>>> 
>>> 
>>> g=OrderedDict()
>>> g['d']=4
>>> g['b']=2
>>> g['a']=1
>>> g['c']=3
>>> g['e']=5
>>> g
OrderedDict([('d', 4), ('b', 2), ('a', 1), ('c', 3), ('e', 5)])
>>> 
>>> 
>>> g.popitem(last=False)
('d', 4)
>>> g
OrderedDict([('b', 2), ('a', 1), ('c', 3), ('e', 5)])
>>> g.popitem(last=True)
('e', 5)
>>> g
OrderedDict([('b', 2), ('a', 1), ('c', 3)])
>>>>>>> 847eeaabd6bbfccc5f4943ee15aafb32dc78368a
>>> 