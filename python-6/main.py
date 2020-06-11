from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    @abstractmethod
    def calc_bonus(self):
        pass

    #@abstractmethod
    def get_hours(self):
        return 8
    
    def get_department(self):
        pass

    def set_department(self, department):
        pass

class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_department(self):
        return self.__department.name

    def set_department(self, department):
        self.__department.name = department


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.get_sales() * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        self.__sales += sale

    def get_department(self):
        return self.__department.name

    def set_department(self, department):
        self.__department.name = department