"""
First class function
"""
def square(x):
    return x*x

f=square        #like function pointer

print(square)   #address of function
print(f(5))      #excute the function

def my_map(func, arglist):
    result=[]
    for i in arglist:
        result.append(func(i))
    return result

squares=my_map(square, [1,2,3,4,5])

print(squares)

def cube(x):
    return x*x*x

cubes=my_map(cube, [1,2,3,4,5])
print(cubes)


def logger(msg):
    def log_message():
        print('Log:', msg)

    return log_message

log_hi=logger('Hi all')
log_hi()


def html_tag(tag):

    def wrap_test(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_test


print_h1=html_tag('h1') #Calling html_tag
print_h1("test headine") #callin wrap_test



#Clousres

def outer_func(msg):
    message=msg

    def inner_func():
        print (message)

    return inner_func


my_func1=outer_func('Hi')
my_func2 = outer_func('Tata')

my_func1()
my_func2()

def newlogger(func):
    def log_func(*args):
        print(func(*args))
    return log_func


def add1(x, y):
    return x+y

def add2(x,y,z):
    return x+y+z

newlog1=newlogger(add1)
newlog2=newlogger(add2)

newlog1(3,4)
newlog2(5,6,7)


#decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper function")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Ran successfully")

#same as
#display=decorator_function(display)

display()


@decorator_function
def display_args(x,y):
    print("Ran successfully {} and {}".format(x,y))


display_args(3,4)
