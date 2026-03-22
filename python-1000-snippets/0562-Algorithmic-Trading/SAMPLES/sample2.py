# sample2.py
# Simulate trading based on moving average strategy.


def simulate_trading(prices, window=2):
    signals = []
    for i in range(window, len(prices)):
        current = prices[i]
        ma = sum(prices[i-window:i]) / window
        signals.append({'index': i, 'price': current, 'signal': current > ma})
    return signals


if __name__ == '__main__':
    prices = [100, 101, 102, 103, 104]
    print('Signals:', simulate_trading(prices))
