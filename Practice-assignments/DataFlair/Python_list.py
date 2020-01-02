Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> colors=['red','green','blue']
>>> colors
['red', 'green', 'blue']
>>> days=['Monday','Tuesday','Wednesday',4,5,6,7.0]
>>> days
['Monday', 'Tuesday', 'Wednesday', 4, 5, 6, 7.0]
>>> languages=[['English'],['Gujarati'],['Hindi'],'Romanian','Spanish']
>>> languages
[['English'], ['Gujarati'], ['Hindi'], 'Romanian', 'Spanish']
>>> type(colors)
<class 'list'>
>>> type(days)
<class 'list'>
>>> type(languages)
<class 'list'>
>>> type(languages[0])
<class 'list'>
>>> for elem in languages:
	print (elem)
	print(type(elem))

	
['English']
<class 'list'>
['Gujarati']
<class 'list'>
['Hindi']
<class 'list'>
Romanian
<class 'str'>
Spanish
<class 'str'>
>>> indices=['zero','one','two','three','four','five']
>>> indices[2:4]
['two', 'three']
>>> indices[:4]
['zero', 'one', 'two', 'three']
>>> indices[4:]
['four', 'five']
>>> indices[:-2]
['zero', 'one', 'two', 'three']
>>> indices[1:-2]
['one', 'two', 'three']
>>> indices[-2:-1]
['four']
>>> indices[-1:-2]
[]
>>> colors[2:]=['bronze','silver']
>>> colors
['red', 'green', 'bronze', 'silver']
>>> colors=['caramel','gold','silver','occur']
>>> colors
['caramel', 'gold', 'silver', 'occur']
>>> colors[2:3]=['bronze','silver']
>>> colors
['caramel', 'gold', 'bronze', 'silver', 'occur']
>>> colors[2:2]=['occur']
>>> colors
['caramel', 'gold', 'occur', 'bronze', 'silver', 'occur']
>>> colors[3]='bronze'
>>> colors
['caramel', 'gold', 'occur', 'bronze', 'silver', 'occur']
>>> del colors
>>> colors
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    colors
NameError: name 'colors' is not defined
>>> 
>>> 
>>> colors=['caramel','gold','silver','bronze','holographic']
>>> del colors[2:4]
>>> coors
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    coors
NameError: name 'coors' is not defined
>>> colors
['caramel', 'gold', 'holographic']
>>> 
>>> 
>>> 
>>> del colors[0]
>>> colors
['gold', 'holographic']
>>> 
>>> 
>>> grocery_list=[['caramel','P&B','Jelly'],['onions','potatoes'],['flour','oil']]
>>> grocery_list
[['caramel', 'P&B', 'Jelly'], ['onions', 'potatoes'], ['flour', 'oil']]
>>> 
>>> type(grocery_list)
<class 'list'>
>>> 
>>> 
>>> for elem in grocery_list:
	print(elem)
	print(type(elem))

	
['caramel', 'P&B', 'Jelly']
<class 'list'>
['onions', 'potatoes']
<class 'list'>
['flour', 'oil']
<class 'list'>
>>> 
>>> 
>>> a=[[[1,2],[3,4],5],[6,7]]
>>> a
[[[1, 2], [3, 4], 5], [6, 7]]
>>> for x in a:
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> 
>>> 
>>> for x in a:
	print (x)
	print (type(x))

	
[[1, 2], [3, 4], 5]
<class 'list'>
[6, 7]
<class 'list'>
>>> 
>>> 
>>> a[0][1][1]
4
>>> a,b=[3,1,2],[5,4,6]
>>> a
[3, 1, 2]
>>> b
[5, 4, 6]
>>> a+b
[3, 1, 2, 5, 4, 6]
>>> c=a.append(b)
>>> c
>>> a
[3, 1, 2, [5, 4, 6]]
>>> a=a*3
>>> a
[3, 1, 2, [5, 4, 6], 3, 1, 2, [5, 4, 6], 3, 1, 2, [5, 4, 6]]
>>> 4 in a
False
>>> 1 in a
True
>>> 4 in a[1]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    4 in a[1]
TypeError: argument of type 'int' is not iterable
>>> type(a)
<class 'list'>
>>> 4 in a[3]
True
>>> a[3]
[5, 4, 6]
>>> for x in a:
	type("{}   {}".format(x, type(x)))

	
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
>>> for x in a:
	print(x)

	
3
1
2
[5, 4, 6]
3
1
2
[5, 4, 6]
3
1
2
[5, 4, 6]
>>> for x in a:
	print(type(x))

	
<class 'int'>
<class 'int'>
<class 'int'>
<class 'list'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'list'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'list'>
>>> 
>>> 
>>> 
>>> for in in [1,2,3]:
	
SyntaxError: invalid syntax
>>> for i in [1,2,3]:
	if i%2==0:
		print(i)

		
2
>>> 
>>> 
>>> even=[2*i for i in range(1,11)]
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> 
>>> 
>>> 
>>> 
>>> len(even)
10
>>> 
>>> 
>>> max(even)
20
>>> 
>>> colors=['red','blue','green','orange',['a','b','c']]
>>> colors
['red', 'blue', 'green', 'orange', ['a', 'b', 'c']]
>>> len(colors)
5
>>> 
>>> max(colors)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    max(colors)
TypeError: '>' not supported between instances of 'list' and 'str'
>>> 
>>> numbers=['1','2','3']
>>> max(numbers)
'3'
>>> 
>>> 
>>> min(numbers)
'1'
>>> 
>>> min(even)
2
>>> 
>>> min
<built-in function min>
(
>>> min(colors)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    min(colors)
TypeError: '<' not supported between instances of 'list' and 'str'
>>> 
>>> 
>>> sum(even)
110
>>> 
>>> 
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> sum(numbers)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    sum(numbers)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> sum(colors)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    sum(colors)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> sorted(colors)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    sorted(colors)
TypeError: '<' not supported between instances of 'list' and 'str'
>>> 
>>> 
>>> colors=['red','blue','green']
>>> min(colors)
'blue'
>>> max(colors)
'red'
>>> sorted(colors)
['blue', 'green', 'red']
>>> 
>>> 
>>> x=list("abc")
>>> x
['a', 'b', 'c']
>>> any[['','',1]]
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    any[['','',1]]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> any(['','','1'])
True
>>> any([0,0,0])
False
>>> any([0,0,2])
True
>>> any([])
False
>>> 
>>> 
>>> all([])
True
>>> all([0,0,0])
False
>>> all([0,0,1])
False
>>> all([1,1,2])
True
>>> a=[1,2,3]
>>> a
[1, 2, 3]
>>> a.append('blue')
>>> a
[1, 2, 3, 'blue']
>>> a.append(['1','2'])
>>> a
[1, 2, 3, 'blue', ['1', '2']]
>>> 
>>> 
>>> 
>>> a.insert(2, 'v')
>>> a
[1, 2, 'v', 3, 'blue', ['1', '2']]
>>> 
>>> 
>>> a.insert(3, ['x','y','z'])
>>> a
[1, 2, 'v', ['x', 'y', 'z'], 3, 'blue', ['1', '2']]
>>> 
>>> 
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    a.remove(5)
ValueError: list.remove(x): x not in list
>>> a.remove('v')
>>> a
[1, 2, ['x', 'y', 'z'], 3, 'blue', ['1', '2']]
>>> 
>>> 
>>> a.pop()
['1', '2']
>>> a
[1, 2, ['x', 'y', 'z'], 3, 'blue']
>>> a.pop()
'blue'
>>> a
[1, 2, ['x', 'y', 'z'], 3]
>>> 
>>> 
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    a.index()
TypeError: index expected at least 1 argument, got 0
>>> a.index(3)
3
>>> a
[1, 2, ['x', 'y', 'z'], 3]
>>> a.index(2)
1
>>> a.clear()
>>> a
[]
>>> 
>>> 
>>> 
>>> a=[1,2,3,['x','y','z'],'blue', '123456']
>>> a
[1, 2, 3, ['x', 'y', 'z'], 'blue', '123456']
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>> a.count(2)
1
>>> a.count(2)
1
>>> a.count('x')
0
>>> a.count('blue')
1
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> 
>>> 
>>> x=['a','b','c']
>>> y=[1,2,3,0,,9,6]
SyntaxError: invalid syntax
>>> y=[1,2,3,0,9,6]
>>> x
['a', 'b', 'c']
>>> y
[1, 2, 3, 0, 9, 6]
>>> x.sort()
>>> x
['a', 'b', 'c']
>>> y.sort()
>>> y
[0, 1, 2, 3, 6, 9]
>>> z=[6,7,8,[1,2,3]]
>>> z.sort()
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    z.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> 
>>> 
>>> 
>>> 
>>> languages=['C++','Python','Scratch']
>>> languages
['C++', 'Python', 'Scratch']
>>> 
>>> 
>>> list1=[1,[2,3],(4,5),False,'No']
>>> list1
[1, [2, 3], (4, 5), False, 'No']
>>> 
>>> 
>>> list1[3]
False
>>> 
>>> type(list1[-2])
<class 'bool'>
>>> 
>>> list1[1:4]
[[2, 3], (4, 5), False]
>>> 
>>> 
>>> list1[:-2]
[1, [2, 3], (4, 5)]
>>> languages[2]='Java'
>>> 
>>> languages
['C++', 'Python', 'Java']
>>> 
>>> list1
[1, [2, 3], (4, 5), False, 'No']
>>> 
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> 
>>> 
>>> languages
['C++', 'Python', 'Java']
>>> del languages[2]
>>> languages
['C++', 'Python']
>>> 
>>> 
>>> languages[0]='C'
>>> languages
['C', 'Python']
>>> 
>>> list1=[1,2,3,4,5,6,7,8]
>>> list1[1:3]=[9,10,11]
>>> list1
[1, 9, 10, 11, 4, 5, 6, 7, 8]
>>> 
>>> 
>>> list1=[0,0,0]
>>> list1
[0, 0, 0]
>>> 
>>> 
>>> 
>>> #List compehension
>>> 
>>> mylist=[]
>>> 
>>> mylist=[i for i in 'anxiety']
>>> mylist
['a', 'n', 'x', 'i', 'e', 't', 'y']
>>> [i*2 for i in {3,1,2}]
[2, 4, 6]
>>> 
>>> 
>>> myset={3,1,2}
>>> 
>>> makelist=lambda i:list(i)
>>> 
>>> 
>>> makelist
<function <lambda> at 0x02BCBD18>
>>> mylist=makelist(myset)
>>> 
>>> mylist
[1, 2, 3]
>>> 
>>> 
>>> 
>>> mylist=[lambda i :list(i)]
>>> mylist
[<function <lambda> at 0x02BCE4A8>]
>>> mylist=makelist(myset)
>>> 
>>> 
>>> mylist
[1, 2, 3]
>>> 
>>> type(mylist)
<class 'list'>
>>> 
>>> 
>>> [i for i in range(8) if i%2!=0]
[1, 3, 5, 7]
>>> 
>>> 
>>> [i for i in range(8) if i%2==0 if i%3==0]
[0, 6]
>>> 
>>> 
>>> ["Even" if i%2==0 else "Odd" for i in range(8)]
['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i in range(7,9):
	for j in range(1,11):
		print(f"{i}*{j}={i*j}")

		
7*1=7
7*2=14
7*3=21
7*4=28
7*5=35
7*6=42
7*7=49
7*8=56
7*9=63
7*10=70
8*1=8
8*2=16
8*3=24
8*4=32
8*5=40
8*6=48
8*7=56
8*8=64
8*9=72
8*10=80
>>> 
>>> 
>>> 
>>> [i*j for j in range(1,11) for in in range(7,9)]
SyntaxError: invalid syntax
>>> [[i*j for j in range (1,11)] for i in range (7,9)]
[[7, 14, 21, 28, 35, 42, 49, 56, 63, 70], [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]]
>>> 
>>> 
>>> 
>>> 
>>> 