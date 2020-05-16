<<<<<<< HEAD
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> colors=('Red','Green','Blue')
>>> colors
('Red', 'Green', 'Blue')
>>> type(colors)
<class 'tuple'>
>>> 
>>> 
>>> mytuple=1,2,3,
>>> mytuple
(1, 2, 3)
>>> type(mytuple)
<class 'tuple'>
>>> a,b,c=mytuple
>>> a
1
>>> b
2
>>> c
3
>>> a=(1)
>>> a
1
>>> type(a)
<class 'int'>
>>> a=(1,)
>>> a
(1,)
>>> type(a)
<class 'tuple'>
>>> 
>>> 
>>> percentages=(90,95,89)
>>> percentages
(90, 95, 89)
>>> 
>>> 
>>> b= 1, 2.0, 'three'
>>> b
(1, 2.0, 'three')
>>> 
>>> 
>>> percentages=(99,95,90,89,93,96)
>>> 
>>> a,b,c,d,e,f=percentages
>>> 
>>> a
99
>>> b
95
>>> c
90
>>> d
89
>>> e
93
>>> f
96
>>> a=1,
>>> type(a)
<class 'tuple'>
>>> 
>>> 
>>> a
(1,)
>>> percentages[1]
95
>>> percentages
(99, 95, 90, 89, 93, 96)
>>> 
>>> percentages[2:4]
(90, 89)
>>> 
>>> 
>>> percentages[:4]
(99, 95, 90, 89)
>>> 
>>> 
>>> percentages[4:]
(93, 96)
>>> 
>>> 
>>> percentages[:-2]
(99, 95, 90, 89)

>>> percentages[-2:]
(93, 96)
>>> 
>>> percentages[:]
(99, 95, 90, 89, 93, 96)
>>> 
>>> 
>>> del percentages[4]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    del percentages[4]
TypeError: 'tuple' object doesn't support item deletion
>>> 
>>> 
>>> del percentages
>>> 
>>> percentages
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    percentages
NameError: name 'percentages' is not defined
>>> 
>>> 
>>> my_tuple=(1,2,3,[4,5])
>>> 
>>> my_tuple
(1, 2, 3, [4, 5])
>>> 
>>> 
>>> my_tuple[3]=6
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    my_tuple[3]=6
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 

>>> my_tuple[3][0]=6
>>> 
>>> 
>>> my_tuple
(1, 2, 3, [6, 5])
>>> 
>>> 
>>> len(my_tuple)
4
>>> 
>>> 
>>> my_tuple
(1, 2, 3, [6, 5])
>>> 
>>> my_tuple.max()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    my_tuple.max()
AttributeError: 'tuple' object has no attribute 'max'
>>> max(my_tuple)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    max(my_tuple)
TypeError: '>' not supported between instances of 'list' and 'int'
>>> a=(1,2,3,4)
>>> a.max()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.max()
AttributeError: 'tuple' object has no attribute 'max'
>>> max(a)
4
>>> 
>>> 
>>> max(('Hi','All', 'Hola'))
'Hola'
>>> 
>>> min(a)
1
>>> 
>>> sum(a)
10
>>> a
(1, 2, 3, 4)
>>> any(a)
True
>>> all(a)
True
>>> any(('','','k'))
True
>>> all(('','','k'))
False
>>> 
>>> sorted(a)
[1, 2, 3, 4]
>>> a
(1, 2, 3, 4)
>>> x=sorted(a)
>>> type(x)
<class 'list'>
>>> x
[1, 2, 3, 4]
>>> string1='Ankit'
>>> tuple(string1)
('A', 'n', 'k', 'i', 't')
>>> set1={2,1,3}
>>> tuple(set1)
(1, 2, 3)
>>> 
>>> a=(1,2,5,6,7,3)
>>> a
(1, 2, 5, 6, 7, 3)
>>> 
>>> 
>>> a.index(2)
1
>>> 
>>> 
>>> a.count(2)
1
>>> 
>>> 'a' in tuple(string1)
False
>>> 'A' in tuple(string1)
True
>>> 
>>> a=(1,2,3)
>>> b=(6,7,8)
>>> a+b
(1, 2, 3, 6, 7, 8)
>>> a=(1,2,3,)
>>> a
(1, 2, 3)
>>> b=('hi','hello')
>>> a+b
(1, 2, 3, 'hi', 'hello')
>>> 
>>> 
>>> (1,2,3)<(4,5,0)
True
>>> (1,2,3)>(4,5,0)
False
>>> a=(1,2)
>>> (1,) is a
False
>>> (1,2) is a
False
>>> 
>>> 
>>> a
(1, 2)
>>> b
('hi', 'hello')
>>> c=a+b
>>> for elem in c:
	print (elem)

	
1
2
hi
hello
>>> a=((1,2,3),[4,5,6],(78,9),('hi','how'))
>>> a
((1, 2, 3), [4, 5, 6], (78, 9), ('hi', 'how'))
>>> a[1][1][1]
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a[1][1][1]
TypeError: 'int' object is not subscriptable
>>> a[1][1]
5
=======
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> colors=('Red','Green','Blue')
>>> colors
('Red', 'Green', 'Blue')
>>> type(colors)
<class 'tuple'>
>>> 
>>> 
>>> mytuple=1,2,3,
>>> mytuple
(1, 2, 3)
>>> type(mytuple)
<class 'tuple'>
>>> a,b,c=mytuple
>>> a
1
>>> b
2
>>> c
3
>>> a=(1)
>>> a
1
>>> type(a)
<class 'int'>
>>> a=(1,)
>>> a
(1,)
>>> type(a)
<class 'tuple'>
>>> 
>>> 
>>> percentages=(90,95,89)
>>> percentages
(90, 95, 89)
>>> 
>>> 
>>> b= 1, 2.0, 'three'
>>> b
(1, 2.0, 'three')
>>> 
>>> 
>>> percentages=(99,95,90,89,93,96)
>>> 
>>> a,b,c,d,e,f=percentages
>>> 
>>> a
99
>>> b
95
>>> c
90
>>> d
89
>>> e
93
>>> f
96
>>> a=1,
>>> type(a)
<class 'tuple'>
>>> 
>>> 
>>> a
(1,)
>>> percentages[1]
95
>>> percentages
(99, 95, 90, 89, 93, 96)
>>> 
>>> percentages[2:4]
(90, 89)
>>> 
>>> 
>>> percentages[:4]
(99, 95, 90, 89)
>>> 
>>> 
>>> percentages[4:]
(93, 96)
>>> 
>>> 
>>> percentages[:-2]
(99, 95, 90, 89)

>>> percentages[-2:]
(93, 96)
>>> 
>>> percentages[:]
(99, 95, 90, 89, 93, 96)
>>> 
>>> 
>>> del percentages[4]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    del percentages[4]
TypeError: 'tuple' object doesn't support item deletion
>>> 
>>> 
>>> del percentages
>>> 
>>> percentages
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    percentages
NameError: name 'percentages' is not defined
>>> 
>>> 
>>> my_tuple=(1,2,3,[4,5])
>>> 
>>> my_tuple
(1, 2, 3, [4, 5])
>>> 
>>> 
>>> my_tuple[3]=6
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    my_tuple[3]=6
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 

>>> my_tuple[3][0]=6
>>> 
>>> 
>>> my_tuple
(1, 2, 3, [6, 5])
>>> 
>>> 
>>> len(my_tuple)
4
>>> 
>>> 
>>> my_tuple
(1, 2, 3, [6, 5])
>>> 
>>> my_tuple.max()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    my_tuple.max()
AttributeError: 'tuple' object has no attribute 'max'
>>> max(my_tuple)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    max(my_tuple)
TypeError: '>' not supported between instances of 'list' and 'int'
>>> a=(1,2,3,4)
>>> a.max()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.max()
AttributeError: 'tuple' object has no attribute 'max'
>>> max(a)
4
>>> 
>>> 
>>> max(('Hi','All', 'Hola'))
'Hola'
>>> 
>>> min(a)
1
>>> 
>>> sum(a)
10
>>> a
(1, 2, 3, 4)
>>> any(a)
True
>>> all(a)
True
>>> any(('','','k'))
True
>>> all(('','','k'))
False
>>> 
>>> sorted(a)
[1, 2, 3, 4]
>>> a
(1, 2, 3, 4)
>>> x=sorted(a)
>>> type(x)
<class 'list'>
>>> x
[1, 2, 3, 4]
>>> string1='Ankit'
>>> tuple(string1)
('A', 'n', 'k', 'i', 't')
>>> set1={2,1,3}
>>> tuple(set1)
(1, 2, 3)
>>> 
>>> a=(1,2,5,6,7,3)
>>> a
(1, 2, 5, 6, 7, 3)
>>> 
>>> 
>>> a.index(2)
1
>>> 
>>> 
>>> a.count(2)
1
>>> 
>>> 'a' in tuple(string1)
False
>>> 'A' in tuple(string1)
True
>>> 
>>> a=(1,2,3)
>>> b=(6,7,8)
>>> a+b
(1, 2, 3, 6, 7, 8)
>>> a=(1,2,3,)
>>> a
(1, 2, 3)
>>> b=('hi','hello')
>>> a+b
(1, 2, 3, 'hi', 'hello')
>>> 
>>> 
>>> (1,2,3)<(4,5,0)
True
>>> (1,2,3)>(4,5,0)
False
>>> a=(1,2)
>>> (1,) is a
False
>>> (1,2) is a
False
>>> 
>>> 
>>> a
(1, 2)
>>> b
('hi', 'hello')
>>> c=a+b
>>> for elem in c:
	print (elem)

	
1
2
hi
hello
>>> a=((1,2,3),[4,5,6],(78,9),('hi','how'))
>>> a
((1, 2, 3), [4, 5, 6], (78, 9), ('hi', 'how'))
>>> a[1][1][1]
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a[1][1][1]
TypeError: 'int' object is not subscriptable
>>> a[1][1]
5
>>>>>>> 847eeaabd6bbfccc5f4943ee15aafb32dc78368a
>>> 