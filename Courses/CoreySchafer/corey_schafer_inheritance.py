class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.__first = first
        self.__last = last
        self.__pay = pay
        self.__email = first + '.' + last + '@company.com'

    def get_email(self):
        return self.__email

    def get_info(self):
        print("Name :{} {}, Salary {}, Email {}".format(
            self.__first, self.__last, self.__pay, self.__email))

    def apply_raise(self):
        self.__pay = int(self.__pay + self.__pay*Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    def __repr__(self):
        return "Employee('{}','{}','{})".format(self.__first, self.__last, self.__pay)

    def __str__(self):
        return "'{}','{}','{}".format(self.__first, self.__last, self.__pay)

    def __add__(self, other):
        return self.__pay+other.__pay

class Developer(Employee):
    raise_amt=1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.__proglang=prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.__employees=[]
        else:
            self.__employees=employees


    def add_employee(self, emp):
        if emp not in self.__employees:
            self.__employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.__employees:
            self.__employees.remove(emp)


    def print_emps(self):
        for emp in self.__employees:
            print(emp.get_info())


dev1 = Developer('XXX','YYY', 50000, 'C')
dev2 = Developer('ZZZZ', 'RRR', 60000, 'Python')

#print(help(Developer))   #get info on method resolution order


#print(dev1.get_info())
#dev1.apply_raise()
#print(dev1.get_info())

mgr_1=Manager('Sue', 'Smith', 90000, [dev1])
print(mgr_1.get_email())

print(mgr_1.print_emps())

mgr_1.add_employee(dev2)
print(mgr_1.print_emps())


mgr_1.remove_employee(dev1)
print(mgr_1.print_emps())

print(dev1.__repr__())
print(dev2.__str__())


print(dev1.__add__(dev2))