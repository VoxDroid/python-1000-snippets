# sample2.py
# Simulate simple pressure and humidity evolution.


def simulate_weather(steps=10):
    pressure = 1013.25
    humidity = 50.0
    out = []
    for i in range(steps):
        pressure += (-0.2 if i % 3 == 0 else 0.1)
        humidity += (1.0 if i % 2 == 0 else -0.5)
        humidity = max(0, min(100, humidity))
        out.append((round(pressure, 2), round(humidity, 1)))
    return out


def main() -> None:
    track = simulate_weather()
    print('First values:', track[:4])
    print('Last values:', track[-4:])


if __name__ == '__main__':
    main()
