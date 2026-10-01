# Author: ChatGPT (reference example for Rithik Saini)
# Date: 10/01/2026
# Name: invoice.py
# Description: Store invoice details and calculate the amount due.
# AI acknowledgment: ChatGPT generated this reference code.

from payroll.payable import Payable


class Invoice(Payable):
    _invoice_count = 0

    def __init__(self, part_name, price, quantity):
        self._part_name = part_name
        self._price = price
        self._quantity = quantity
        Invoice._invoice_count += 1

    def calculate_payment(self):
        return self._price * self._quantity

    def to_dict(self):
        return {
            "type": "Invoice",
            "part_name": self._part_name,
            "price": self._price,
            "quantity": self._quantity,
            "payment": self.calculate_payment()
        }

    @classmethod
    def get_invoice_count(cls):
        return cls._invoice_count
