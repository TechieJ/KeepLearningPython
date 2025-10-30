class LoggableMixin:
    """Adds logging capability."""
    def log(self, message):
        print(f"[LOG]: {message}")


class TimestampMixin:
    """Adds timestamp functionality."""
    from datetime import datetime
    def get_timestamp(self):
        return self.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class SerializableMixin:
    """Adds simple serialization (to_dict)."""
    def to_dict(self):
        return self.__dict__


class User(LoggableMixin, TimestampMixin, SerializableMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        self.log(f"Saving user {self.username} at {self.get_timestamp()}")
        # Imagine saving to DB here...
        print("User saved successfully!")


user = User("jaideep", "jd@example.com")
user.save()
print(user.to_dict())
