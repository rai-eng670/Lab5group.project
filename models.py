# Author: ChatGPT (reference example for Rithik Saini)
# Date: 10/01/2026
# Name: models.py
# Description: Define personal information and the employee class hierarchy.
# AI acknowledgment: ChatGPT generated this reference code.

from abc import abstractmethod
from payroll.payable import Payable


class Person:
    def __init__(self, first_name, last_name, gender, ssn):
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._ssn = ssn

    def to_dict(self):
        return {
            "first_name": self._first_name,
            "last_name": self._last_name,
            "gender": self._gender,
            "ssn": self._ssn
        }


class Employee(Payable):
    _employee_count = 0

    def __init__(self, person, emp_id, years_of_service):
        # Composition: each employee has a Person object.
        self._person = person
        self._emp_id = emp_id
        self._years_of_service = years_of_service
        Employee._employee_count += 1

    @abstractmethod
    def calculate_payment(self):
        pass

    def to_dict(self):
        data = self._person.to_dict()
        data.update({
            "emp_id": self._emp_id,
            "years_of_service": self._years_of_service,
            "payment": self.calculate_payment()
        })
        return data

    @classmethod
    def get_employee_count(cls):
        return cls._employee_count


class Secretary(Employee):
    def __init__(self, person, emp_id, years_of_service, wage, hours):
        super().__init__(person, emp_id, years_of_service)
        self._wage = wage
        self._hours = hours

    def calculate_payment(self):
        return self._wage * self._hours

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Secretary",
            "wage": self._wage,
            "hours": self._hours
        })
        return data


class Manager(Employee):
    def __init__(self, person, emp_id, years_of_service, department,
                 salary):
        super().__init__(person, emp_id, years_of_service)
        self._department = department
        self._salary = salary

    def calculate_payment(self):
        return self._salary

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Manager",
            "department": self._department,
            "salary": self._salary
        })
        return data


class SalesPerson(Employee):
    def __init__(self, person, emp_id, years_of_service, sales,
                 commission_rate):
        super().__init__(person, emp_id, years_of_service)
        self._sales = sales
        self._commission_rate = commission_rate

    def calculate_payment(self):
        return self._sales * self._commission_rate

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Sales Person",
            "sales": self._sales,
            "commission_rate": self._commission_rate
        })
        return data


class ExecutiveManager(Manager):
    def __init__(self, person, emp_id, years_of_service, department,
                 salary, bonus):
        super().__init__(person, emp_id, years_of_service, department,
                         salary)
        self._bonus = bonus

    def calculate_payment(self):
        return super().calculate_payment() + self._bonus

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Executive Manager",
            "bonus": self._bonus
        })
        return data
