"""
Exercise 5: Multiple Inheritance & MRO
"""

class BaseDevices:
    def status(self):
        pass


class WiFiEnabled(BaseDevices):

    @staticmethod
    def connect_wifi():
        print("Connected to Wifi network.")

    def status(self):
        print("WiFi module active.")
        super().status()


class BluetoothEnabled(BaseDevices):
    @staticmethod
    def connect_bluetooth():
        print("Connected via Bluetooth.")

    def status(self):
        print("Bluetooth module active.")
        super().status()


class SmartSpeaker(WiFiEnabled, BluetoothEnabled):
    @staticmethod
    def play_music():
        print("Playing music")

    def status(self):
        print("SmartSpeaker status check:")
        super().status()


ss = SmartSpeaker()
ss.connect_wifi()
ss.connect_bluetooth()
ss.status()
ss.play_music()
print(SmartSpeaker.__mro__)