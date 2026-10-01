# Author: ChatGPT (reference example for Rithik Saini)
# Date: 10/01/2026
# Name: payable.py
# Description: Define the shared contract for payable objects.
# AI acknowledgment: ChatGPT generated this reference code.

from abc import ABC, abstractmethod


class Payable(ABC):
    @abstractmethod
    def calculate_payment(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
