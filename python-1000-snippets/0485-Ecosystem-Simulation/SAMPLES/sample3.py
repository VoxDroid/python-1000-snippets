# sample3.py
# Evaluate equilibrium condition from Lotka-Volterra model and show stability checks.


def lotka_volterra(prey, predator, ap=0.1, bp=0.01, cp=0.005, dp=0.05):
    dprey = prey * (ap - bp * predator)
    dpred = predator * (cp * prey - dp)
    return dprey, dpred


def main() -> None:
    prey, predator = 100, 10
    dprey, dpred = lotka_volterra(prey, predator)
    print('dprey:', round(dprey, 2), 'dpred:', round(dpred, 2))
    print('Equilibrium decisions: prey->', 'grow' if dprey > 0 else 'decline',
          ', predator->', 'grow' if dpred > 0 else 'decline')


if __name__ == '__main__':
    main()
