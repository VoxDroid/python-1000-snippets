# sample3.py
# Evaluate a basic wind chill index and display values.


def wind_chill(temp_c, wind_kmh):
    return 13.12 + 0.6215 * temp_c - 11.37 * (wind_kmh ** 0.16) + 0.3965 * temp_c * (wind_kmh ** 0.16)


def main() -> None:
    temps = [0, 5, 10]
    winds = [5, 15, 30]
    for t in temps:
        for w in winds:
            wc = wind_chill(t, w)
            print(f'T={t}C, W={w}km/h -> chill={wc:.1f}C')


if __name__ == '__main__':
    main()
