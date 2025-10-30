from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, event: str, data: dict):
        pass


class PaymentProcessor:
    def __init__(self):
        self._observers = []

    def register_observers(self, observer: Observer):
        self._observers.append(observer)

    def remove_observers(self, observer: Observer):
        self._observers.remove(observer)

    def _notify_observers(self, event: str, data: dict):
        for observer in self._observers:
            observer.update(event, data)

    def process_payment(self, payment_method, amount):
        result = payment_method.make_payment(amount)
        self._notify_observers("payment_success", {"method": payment_method, "amount": amount})
        return result


class EmailNotifier(Observer):
    def update(self, event: str, data: dict):
        if event == "payment_success":
            print(f"[EmailNotifier] Sent email: Payment of ₹{data['amount']} successful!")


class SMSNotifier(Observer):
    def update(self, event: str, data: dict):
        if event == "payment_success":
            print(f"[SMSNotifier] Sent SMS: Payment of ₹{data['amount']} successful!")


class RewardsSystem(Observer):
    def update(self, event: str, data: dict):
        if event == "payment_success":
            reward = data['amount'] * 0.01
            print(f"[ReawrdSystem] Credited ₹{reward:.2f} as reward points.")


class CreditCardPayment:
    def __init__(self, card_holder):
        self.card_holder = card_holder

    def make_payment(self, amount):
        print(f"Paid ₹{amount} using credit card by {self.card_holder}")


processor = PaymentProcessor()
processor.register_observers(EmailNotifier())
processor.register_observers(SMSNotifier())
processor.register_observers(RewardsSystem())

processor.process_payment(CreditCardPayment("John"), 5000)
