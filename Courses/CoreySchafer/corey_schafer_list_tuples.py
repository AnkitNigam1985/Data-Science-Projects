li=[9,1,8,2,7,3,6,5,4]
s_li=sorted(li)

print("Original : ", li)
print("Sorted :" , s_li)

li.sort()
print("Original sorted : ", li)

my_tup=(5,4,3,2,1)
print("Original tuple :", my_tup)
sl_tup=sorted(my_tup)
print("Sorted tuple :", sl_tup)


li=[-6,-5,4,1,2,3]
s_li=sorted(li, key=abs)
print(s_li)

class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1=Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

def e_sort(emp):
    return emp.name

employees=[e1,e2,e3]
s_employees=sorted(employees, key=e_sort)
print(s_employees)