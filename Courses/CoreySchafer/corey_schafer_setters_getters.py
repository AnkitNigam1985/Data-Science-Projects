class Employee:

    def __init__(self, first, last, pay):
        self.__first = first
        self.__last = last
        self.__pay = pay

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.__first, self.__last)

    @property
    def fullname(self):
        return '{} {}'.format(self.__first, self.__last)

    @fullname.setter
    def fullname(self, name):
        first, last=name.split(' ')
        self.__first=first
        self.__last=last

    @fullname.deleter
    def fullname(self):
        print("Deleting Name")
        self.__first=None
        self.__last=None
    
    def get_info(self):
        print("Name :{} {}, Salary {}".format(
            self.__first, self.__last, self.__pay))

    
emp_1=Employee('XXX','YYY', 500)
print(emp_1.email)

emp_1.fullname='Ankit Nigam'
emp_1.get_info()

del emp_1.fullname   #delete the first and last name
emp_1.get_info()