Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> #LAMBDA EXPRESSION
>>> 
>>> 
>>> lambda e:e-2
<function <lambda> at 0x02AEAC40>
>>> downbytwo=lambda e:e-2
>>> downbytwo
<function <lambda> at 0x02B31100>
>>> 
>>> 
>>> 
>>> e(2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    e(2)
NameError: name 'e' is not defined
>>> downbytwo(3)
1
>>> 
>>> downbytwo(1)
-1
>>> 
>>> 
>>> def func1(a=2,b=3):
	print(a,' ',b)

	
>>> func1()
2   3
>>> o=lambda x=1,y=2,z=3:x+y+z
>>> 
>>> o()
6
>>> o(2,3)
8
>>> o(1,2,3)
6
>>> 
>>> 
>>> 
>>> 
>>> a,b=1,2
>>> y=lambda a,b:a+b
>>> y()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    y()
TypeError: <lambda>() missing 2 required positional arguments: 'a' and 'b'
>>> y(q,b)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    y(q,b)
NameError: name 'q' is not defined
>>> y(a,b)
3
>>> 
>>> 
>>> 
>>> 
>>> 
>>> numbers=[0,1,2,3,4,5,6,7,8,9,10]
>>> 
>>> 
>>> list(filter(lambda x:x%3==0,numbers))
[0, 3, 6, 9]
>>> list(map(lambda x:x%3==0,numbers))
[True, False, False, True, False, False, True, False, False, True, False]
>>> 
>>> from functools import reduce
>>> reduce(lambda x,y:y-x,numbers)
5
>>> num=[1,2,3]
>>> reduce(lambda x,y:y-x,num)
2
>>> 