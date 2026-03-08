# sample2.py
# filename filter strategies using functions

def filter_even(nums):
    return [n for n in nums if n % 2 == 0]

def filter_gt10(nums):
    return [n for n in nums if n > 10]

class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    def execute(self, data):
        return self.strategy(data)

if __name__ == '__main__':
    nums = list(range(15))
    ctx = Context(filter_even)
    print('even:', ctx.execute(nums))
    ctx.set_strategy = lambda s: setattr(ctx, 'strategy', s)
    ctx.set_strategy(filter_gt10)
    print('gt10:', ctx.execute(nums))
