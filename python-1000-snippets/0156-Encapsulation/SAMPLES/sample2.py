# sample2.py
# using @property for encapsulation

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 not possible")
        self._temperature = value

if __name__ == '__main__':
    c = Celsius()
    c.temperature = 37
    print('temp', c.temperature)
    try:
        c.temperature = -300
    except ValueError as e:
        print('error', e)    
