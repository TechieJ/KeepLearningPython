"""
Exercise 8 — Interface Segregation & Mixin Pattern
Mixins let you compose behavior in small, reusable chunks.
They avoid deep inheritance chains and follow Interface Segregation — classes only inherit what they need.
Mixins should be stateless, modular, and independent.
They exist only to extend functionality, not define object identity or hold core data.
You never instantiate them, never rely on subclass attributes, and never cram unrelated methods together.
"""
class WiFiMixin:
    def connect_wifi(self):
        print("Connected to Wifi")


class BluetoothMixin:
        def connect_bluetooth(self):
            print("Connected to Bluetooth")


class VoiceControlMixin:
    def activate_voice_control(self):
        print("Voice control activated")


class BatteryPoweredMixin:
    def battery_status(self):
        print("Battery at 80%")


class Device:
    def __init__(self, name):
        self.name = name

    def device_info(self):
        print(f"Device: {self.name}")


class SmartSpeaker(Device, WiFiMixin, BluetoothMixin, VoiceControlMixin):
    pass


class WirelessEarbuds(Device, BluetoothMixin, BatteryPoweredMixin):
    pass


class SmartLight(Device, WiFiMixin):
    pass


class SmartWatch(Device, WiFiMixin, BluetoothMixin, BatteryPoweredMixin, VoiceControlMixin):
    def battery_status(self):
        super().battery_status()
        print("Heart rate: 72 bpm")


speaker = SmartSpeaker("Alexa")
earbuds = WirelessEarbuds("AirPods")
light = SmartLight("Philips Hue")

speaker.device_info()
speaker.connect_wifi()
speaker.activate_voice_control()

earbuds.connect_bluetooth()
earbuds.battery_status()

light.connect_wifi()

smartwatch = SmartWatch("Apple Watch")
smartwatch.battery_status()