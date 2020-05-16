class Employee:
    raise_amount=1.04
    num_of_emps=0
    def __init__(self, first, last, pay):
        self.__first=first
        self.__last=last
        self.__pay=pay
        self.__email=first+'.'+last+'@company.com'

    def get_email(self):
        return self.__email

    def get_info(self):
        print("Name :{} {}, Salary {}, Email {}".format(self.__first, self.__last, self.__pay, self.__email))

    def apply_raise(self):
        self.__pay=int(self.__pay + self.__pay*Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay=emp_str.split('-')
        return cls(first,last, pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        else:
            return True
        

emp1=Employee('XXX','YYY',3000)
emp2=Employee('ABC','DEF', 5000)

print(emp1.get_email())
print(emp2.get_email())

print(emp1.get_info())
print(emp2.get_info())

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)


print(Employee.__dict__)

#Employee.raise_amount=2.04

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

#emp1.raise_amount=5     #raise_amount become instance variable for emp1 rather than Employye class, but not for emp2

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)

Employee.set_raise_amount(5)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

emp1.raise_amount=10     #raise_amount become instance variable for emp1 rather than Employye class, but not for emp2

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

Employee.set_raise_amount(5)    #after emp1.raise_ampount=10, emp1 has seperate raise_amount, so no impact of this
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)


emp_str_1='John-Doe-70000'
emp_str_2 = 'Steve-Smith-60000'
emp_str_3 = 'Carlk-Kent-90000'


new_emp1=Employee.from_string(emp_str_1)
print(new_emp1.get_info())


import datetime
my_date=datetime.date(2019, 7, 20)
print(Employee.is_work_day(my_date))