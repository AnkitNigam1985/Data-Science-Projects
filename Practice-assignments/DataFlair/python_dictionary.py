Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mydict={1:2,2:4,3:6}
>>> mydict
{1: 2, 2: 4, 3: 6}
>>> mydict[2]
4
>>> 
>>> 
>>> {'PB&J':'Peanut Butter and Jelly','PJ':'Pajamas'}
{'PB&J': 'Peanut Butter and Jelly', 'PJ': 'Pajamas'}
>>> 
>>> lingo={'PB&J':'Peanut Butter and Jelly','PJ':'Pajamas'}
>>> 
>>> dict2={}
>>> dict2
{}
>>> 
>>> 
>>> mydict={x*x:x for x in range(8)}
>>> mydict
{0: 0, 1: 1, 4: 2, 9: 3, 16: 4, 25: 5, 36: 6, 49: 7}
>>> 
>>> 
>>> 
>>> dict3={1:'carrots','two':[1,2,3]}
>>> dict3
{1: 'carrots', 'two': [1, 2, 3]}
>>> 
>>> 
>>> 
>>> dict(([1,2],[2,4],[3,6]))
{1: 2, 2: 4, 3: 6}
>>> dict
<class 'dict'>
>>> x=dict(([1,2],[2,4],[3,6]))
>>> dict
<class 'dict'>
>>> x
{1: 2, 2: 4, 3: 6}
>>> mydict2={1:2,1:3,1:4,2:4}
>>> mydict2
{1: 4, 2: 4}
>>> 
>>> 
>>> 
>>> animals={}
>>> type(animals)
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> animals={}
>>> 
>>> animals[1]='dog'
>>> animals[2]='cat'
>>> 
>>> animals
{1: 'dog', 2: 'cat'}
>>> animal.get(1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    animal.get(1)
NameError: name 'animal' is not defined
>>> animals.get(1)
'dog'
>>> animals[1]
'dog'
>>> del animals
>>> 
>>> 
>>> animals
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    animals
NameError: name 'animals' is not defined
>>> 
>>> 
>>> dict2
{}
>>> dict2={[1,2],[3,4]}
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict2={[1,2],[3,4]}
TypeError: unhashable type: 'list'
>>> x=dict(([1,2],[3,4],[5,6]))
>>> x
{1: 2, 3: 4, 5: 6}
>>> x.items()
dict_items([(1, 2), (3, 4), (5, 6)])
>>> x.keys()
dict_keys([1, 3, 5])
>>> x.values()
dict_values([2, 4, 6])
>>> x.fromkeys([1,2])
{1: None, 2: None}
>>> x
{1: 2, 3: 4, 5: 6}
>>> x.fromkeys([6,7],3)
{6: 3, 7: 3}
>>> x
{1: 2, 3: 4, 5: 6}
>>> y=x.fromkeys([1,2])
>>> y
{1: None, 2: None}
>>> y=x.fromkeys([6,7],3)
>>> y
{6: 3, 7: 3}
>>> 