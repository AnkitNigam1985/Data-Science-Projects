class Employee:
    def __init__(self, employee_name, employee_id, shiftnum):
        self.__emp_name=employee_name
        self.__emp_id=employee_id
        self.__emp_shift=shiftnum

    def print_employee_info(self):
        print("Employee name : ", self.__emp_name)
        print("Employee ID : ", self.__emp_id)
        print("Employee shift : ", self.__emp_shift)

    def set_employee_id(self, p_id):
        self.__emp_id=p_id

    def set_employee_name(self, p_name):
        self.__emp_name=p_name

    def set_employee_shift(self, p_shiftnum):
        self.__emp_shift=p_shiftnum


def main():
    my_empobj=Employee("Ankit", 123, 'M')

    my_empobj.print_employee_info()


main()
