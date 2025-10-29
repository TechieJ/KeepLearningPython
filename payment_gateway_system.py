from abc import ABC, abstractmethod


class Payment(ABC):

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


class PayPalPayment(Payment):

    def __init__(self, email):
        self.email = email

    def make_payment(self, amount):
        self.validate_amount(amount)
        print(f"Payment of ₹{amount} done via PayPal for {self.email}")


class UPIPayment(Payment):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def make_payment(self, amount):
        self.validate_amount(amount)
        print(f"Payment of ₹{amount} done via UPI ID {self.upi_id}")


def process_payment(payment_method, amount):
    return payment_method.make_payment(amount)

payments = [
    CreditCardPayment("John", "1234567812345678"),
    PayPalPayment("john@example.com"),
    UPIPayment("john@oksbi")
]

for p in payments:
    process_payment(p, 500)
