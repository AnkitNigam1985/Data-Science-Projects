"""
You given a function  construct(a,b): this function returns a pair. You also given two other functions  which accepts construct(a,b) function as argument the first function named first(), and the second function named last(), the first function return the first element in the given argument, and the last function returns the last element in the given argument. 
For example\ first(construct(1,9) returns 1
		     Last(construct(1,9) returns 9

first(construct(0,1) returns 0
Last(construct(0,1) returns 1
________________________________
If you construct functions defined as this
def construct(a, b):
    def pair(x):
        return x(a, b)
    return pair
Implement both first() function, and last() function
"""

def construct(a, b):
    def pair(x):
        return x(a, b)
    return pair
    
def first(pair):
    def x(a,b):
        return a
    
    return pair(x)
    

def last(pair):
    def x(a,b):
        return b
    return pair(x)

a=int(input('enter the first element'))
b=int(input('enter the last element'))

print('the first is', first(construct(a,b)))
print('the last is', last(construct(a,b)))