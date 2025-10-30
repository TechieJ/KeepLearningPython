"""
Exercise 3 — Abstract Classes & Polymorphism with strategy pattern (behaviour design pattern)
"""


from abc import ABC, abstractmethod
from datetime import datetime


class LoggingMixin:
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG {timestamp}] {message}")


class Payment(ABC, LoggingMixin):

    @abstractmethod
    def make_payment(self, amount):
        pass

    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise ValueError(f"Amount {amount} <= 0")
        print(f"Validated amount: ₹{amount}")


class CreditCardPayment(Payment):

    def __init__(self, card_holder, card_number):
        self.card_number = card_number
        self.card_holder = card_holder

    def make_payment(self, amount):
        self.validate_amount(amount)
        masked_card = self.card_number[-4:]
        print(f"Paid ₹{amount} using credit card (****{masked_card})")
        self.log(f"{self.card_holder} paid ₹{amount} via CreditCardPayment")


class PayPalPayment(Payment):

    def __init__(self, email):
        self.email = email

    def make_payment(self, amount):
        self.validate_amount(amount)
        print(f"Payment of ₹{amount} done via PayPal for {self.email}")
        self.log(f"{self.email} paid ₹{amount} via PayPalPayment")


class UPIPayment(Payment):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def make_payment(self, amount):
        self.validate_amount(amount)
        print(f"Payment of ₹{amount} done via UPI ID {self.upi_id}")
        self.log(f"{self.upi_id} paid ₹{amount} via UPIPayment")


class PaymentProcessor:
    def __init__(self, strategy: Payment):
        self._strategy = strategy

    def set_strategy(self, new_strategy: Payment):
        print(f"Switched payment strategy to {new_strategy.__class__.__name__}")
        self._strategy = new_strategy

    def process_payment(self, amount):
        self._strategy.make_payment(amount)


processor = PaymentProcessor(CreditCardPayment("John", "1234567812345678"))
processor.process_payment(5000)

processor.set_strategy(PayPalPayment("john@example.com"))
processor.process_payment(3500)

processor.set_strategy(UPIPayment("john@oksbi"))
processor.process_payment(15000)
