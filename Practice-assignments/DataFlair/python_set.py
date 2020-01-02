Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myset={3,1,2}
>>> myset
{1, 2, 3}
>>> 
>>> 
>>> a={1,3,2}
>>> a
{1, 2, 3}
>>> c={1,2.0,'three'}
>>> c
{'three', 1, 2.0}
>>> b={3,2,1,2}
>>> b
{1, 2, 3}
>>> d={[1,2,3],4}
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d={[1,2,3],4}
TypeError: unhashable type: 'list'
>>> 
>>> 
>>> 
>>> d=set()
>>> type(d)
<class 'set'>
>>> 
>>> 
>>> d={}
>>> type(d)
<class 'dict'>
>>> 
>>> 
>>> d=set([1,3,2])
>>> 
>>> type(d)
<class 'set'>
>>> 
>>> a
{1, 2, 3}
>>> 
>>> 
>>> c
{'three', 1, 2.0}
>>> 
>>> 
>>> b
{1, 2, 3}
>>> 
>>> 
>>> numbers={3,2,1,4,6,5}
>>> numbers
{1, 2, 3, 4, 5, 6}
>>> 
>>> 
>>> numbers.discard(3)
>>> numbers
{1, 2, 4, 5, 6}
>>> 
>>> 
>>> numbers.remove(3)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    numbers.remove(3)
KeyError: 3
>>> 
>>> 
>>> numbers.discard(3)
>>> 
>>> 
>>> numbers.remove(5)
>>> 
>>> 
>>> numbers
{1, 2, 4, 6}
>>> 
>>> 
>>> numbers.pop()
1
>>> 
>>> 
>>> numbers
{2, 4, 6}
>>> 
>>> 
>>> 
>>> numbers.clear()
>>> 
>>> 
>>> numbers
set()
>>> 
>>> numbers={3,1,2,4,6,5}
>>> 
>>> 
>>> numbers[3]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    numbers[3]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> numbers.add(3,5)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    numbers.add(3,5)
TypeError: add() takes exactly one argument (2 given)
>>> numbers.add(3.5)
>>> 
>>> numbers
{1, 2, 3, 4, 5, 6, 3.5}
>>> numbers.add(4)
>>> 
>>> numbers
{1, 2, 3, 4, 5, 6, 3.5}
>>> 
>>> 
>>> 
>>> numbers.update([7,8],{1,2,9})
>>> 
>>> numbers
{1, 2, 3, 4, 5, 6, 3.5, 7, 8, 9}
>>> 
>>> 
>>> days={'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'}
>>> 
>>> 
>>> len(days)
7

>>> max(days)
'Wednesday'
>>> 
>>> 
>>> min(days)
'Friday'
>>> 
>>> 
>>> sum(days)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    sum(days)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> sum((1,2,3))
6
>>> 
>>> 
>>> any(days)
True
>>> 
>>> 
>>> any((0,0,0))
False
>>> any((1,2,3))
True
>>> all((0,0,1))
False
>>> 
>>> 
>>> all((1,2,3,))
True
>>> sorted(days)
['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
>>> days
{'Wednesday', 'Tuesday', 'Monday', 'Saturday', 'Thursday', 'Sunday', 'Friday'}
>>> 
>>> 
>>> 
>>> 

>>> set1,set2,set3={1,2,3},{3,4,5},{5,6,7}
>>> 
>>> 
>>> 
>>> set1
{1, 2, 3}
>>> 
>>> 
>>> set2
{3, 4, 5}
>>> 
>>> 
>>> set3
{5, 6, 7}

>>> 
>>> set1.union(set2)
{1, 2, 3, 4, 5}
>>> 
>>> 

>>> 
>>> set1.union(set2,set3)
{1, 2, 3, 4, 5, 6, 7}
>>> 
>>> 
>>> set1
{1, 2, 3}
>>> 
>>> 
>>> 
>>> set2.intersection(set1)
{3}
>>> 
>>> set1.difference(set2)
{1, 2}

>>> set1.difference(set2,set3)
{1, 2}
>>> 
>>> 
>>> set1
{1, 2, 3}
>>> set2
{3, 4, 5}
>>> set1.symmetric_difference(set2)
{1, 2, 4, 5}
>>> 
>>> 
>>> set1
{1, 2, 3}
>>> set2
{3, 4, 5}
>>> 
>>> set1.intersection_update(set2)
>>> 
>>> set1
{3}
>>> 
>>> set1={1,2,3}
>>> set2={3,4,5}
>>> 
>>> set1.difference_update(set2)
>>> 
>>> set1
{1, 2}
>>> set2
{3, 4, 5}
>>> 
>>> 

>>> set1={1,2,3}
>>> set2={3,4,5}
>>> 
>>> set1.symmetric_difference_update(set2)
>>> 
>>> 
>>> set1
{1, 2, 4, 5}
>>> set2
{3, 4, 5}
>>> 
>>> 
>>> 
>>> set4=set1.copy()
>>> 
>>> set4
{1, 2, 4, 5}
>>> set1
{1, 2, 4, 5}
>>> {1,3,2}.isdisjoint({4,5,6})   #True if two sets have a null intersection
True
>>> {1,2,3}.isdisjoint({3,4,5})
False
>>> 
>>> 
>>> {1,2}.issubset({1,2,3})
True
>>> 
>>> 
>>> {1,2}.issubset({1,2})
True
>>> 
>>> 
>>> {1,2}.issubset({1})
False
>>> 
>>> 
>>> {1,3,4}.issuperset({1,2})
False
>>> 
>>> 'p' in {'a','p','p','l','e'}
True
>>> 
>>> 0 not in {'0','1'}
True
>>> 
>>> for i in {1,3,2}:
	print(i)

	
1
2
3
>>> 
>>> 
>>> #FROZEN SET
>>> 
>>> #A frozen set is in-effect an immutable set. You cannot change its values. Also, a set can’t be used a key for a dictionary, but a frozenset can
>>> 
>>> 
>>> {{1,2}:3}
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    {{1,2}:3}
TypeError: unhashable type: 'set'

>>> {frozenset(1,2):3}
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    {frozenset(1,2):3}
TypeError: frozenset expected at most 1 argument, got 2
>>> 
>>> {frozenset([1,2]):3}
{frozenset({1, 2}): 3}
>>> 
>>> 
>>> x={frozenset([1,2]):3}
>>> x
{frozenset({1, 2}): 3}
>>> x.keys()
dict_keys([frozenset({1, 2})])
>>> x.values()
dict_values([3])
>>> x.items()
dict_items([(frozenset({1, 2}), 3)])
>>> 
>>> 
>>> 
>>> bool('Wisdom')
True
>>> 
>>> 
>>> bool(0)
False
>>> 
>>> 
>>> bool(' ')
True
>>> 
>>> 
>>> bool((1,3,2))
True
>>> 
>>> 
>>> bool(())
False
>>> 
>>> 
>>> 