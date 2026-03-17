# sample2.py
# Remote control abstraction using bridge to connect to devices

class Device:
    def power_on(self):
        raise NotImplementedError

    def power_off(self):
        raise NotImplementedError


class TV(Device):
    def power_on(self):
        return "TV on"

    def power_off(self):
        return "TV off"


class Radio(Device):
    def power_on(self):
        return "Radio on"

    def power_off(self):
        return "Radio off"


class Remote:
    def __init__(self, device):
        self.device = device

    def toggle_power(self, on):
        if on:
            return self.device.power_on()
        return self.device.power_off()


def main():
    tv_remote = Remote(TV())
    radio_remote = Remote(Radio())
    print(tv_remote.toggle_power(True))
    print(radio_remote.toggle_power(False))


if __name__ == "__main__":
    main()
