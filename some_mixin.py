class WiFiMixin:
    def connect_wifi(self, name):
        print(f"{name} connected to WiFi")


class BluetoothMixin:

    def connect_bluetooth(self, name):
        print(f"{name} connected to Bluetooth")


class AudioMixin:

    def play_music(self, volume):
        print(f"Playing music at volume {volume}")


class LoggingMixin:
    def log_action(self, name, msg):
        print(f"[LOG - {name}]: {msg}")


class SmartDevice:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def device_info(self):
        print(f"Device: {self.name}")

    def battery_status(self):
        print(f"{self.name} battery: {self.battery}%")


class SmartSpeaker(SmartDevice, WiFiMixin, BluetoothMixin, AudioMixin, LoggingMixin):
    def activate(self):
        self.log_action(self.name, "Powering on...")
        self.connect_wifi(self.name)
        self.connect_bluetooth(self.name)
        self.play_music(5)
        self.log_action(self.name, "Ready to use")


class SmartWatch(SmartDevice, WiFiMixin, BluetoothMixin, LoggingMixin):
    def activate(self):
        self.log_action(self.name, "Connecting...")
        self.connect_wifi(self.name)
        self.connect_bluetooth(self.name)
        self.log_action(self.name, "All systems active.")
        self.battery_status()


speaker = SmartSpeaker("Alexa", "72%")
earbuds = SmartWatch("Apple Watch", "80%")

speaker.device_info()
speaker.activate()
