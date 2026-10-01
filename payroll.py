# Author: ChatGPT (reference example for Rithik Saini)
# Date: 10/01/2026
# Name: payroll.py
# Description: Build sample payable objects and summarize their payments.
# AI acknowledgment: ChatGPT generated this reference code.

from payroll.invoice import Invoice
from payroll.models import (
    Employee, Person, Secretary, Manager, SalesPerson, ExecutiveManager
)


def serialize_payroll(payable):
    # Every Payable object responds to this same method call.
    return payable.to_dict()


def build_payroll_data():
    # Record starting counts so refreshes do not inflate this report.
    starting_invoices = Invoice.get_invoice_count()
    starting_employees = Employee.get_employee_count()

    # Fictional people and invalid sample SSNs for this demonstration.
    payables = [
        Invoice("Printer Cartridge", 75.50, 3),
        Invoice("Monitor Stand", 42.99, 2),
        Secretary(
            Person("Alice", "Wong", "Female", "000-00-0101"),
            101, 2, 25.00, 40
        ),
        Manager(
            Person("Thomas", "Cho", "Male", "000-00-0102"),
            102, 8, "IT", 8500.00
        ),
        ExecutiveManager(
            Person("Elena", "Stone", "Female", "000-00-0103"),
            103, 10, "Operations", 12000.00, 2500.00
        ),
        SalesPerson(
            Person("John", "Davis", "Male", "000-00-0104"),
            104, 4, 15000.00, 0.08
        )
    ]

    payables_data = []
    total_gross = 0
    for payable in payables:
        data = serialize_payroll(payable)
        payables_data.append(data)
        total_gross += payable.calculate_payment()

    total_invoices = Invoice.get_invoice_count() - starting_invoices
    total_employees = Employee.get_employee_count() - starting_employees

    return {
        "payables": payables_data,
        "invoice_count": total_invoices,
        "employee_count": total_employees,
        "total_gross": round(total_gross, 2)
    }
