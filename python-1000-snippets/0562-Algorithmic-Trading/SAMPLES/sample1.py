# sample1.py
# Calculate simple moving averages and generate buy signal.


def simple_ma(prices, window=2):
    return [sum(prices[i-window:i]) / window for i in range(window, len(prices)+1)]


def buy_signal(prices, window=2):
    ma = simple_ma(prices, window)
    return prices[-1] > ma[-1]


if __name__ == '__main__':
    prices = [100, 101, 102, 103, 104]
    print('Buy signal:', buy_signal(prices, 2))
