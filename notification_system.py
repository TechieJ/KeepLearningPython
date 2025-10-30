
"""
Exercise 7 — Composition and Polymorphism (Duck Typing in Action)
"""
class EmailService:
    def send(self, message):
        print(f"Email sent: {message}")


class SMSService:
    def send(self, message):
        print(f"SMS sent: {message}")


class PushService:
    def send(self, message):
        print(f"Push notification sent: {message}")


class NotificationManager:

    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send(message)

email = NotificationManager(EmailService())
sms = NotificationManager(SMSService())
push = NotificationManager(PushService())

for manager in [email, sms, push]:
    manager.notify("System maintenance at 9 PM")