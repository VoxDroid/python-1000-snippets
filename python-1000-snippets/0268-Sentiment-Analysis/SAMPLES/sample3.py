# sample3.py
# Use a simple lexicon-based sentiment analyzer to score a batch of sentences.

POSITIVE = {'good', 'great', 'happy', 'love', 'excellent', 'fantastic', 'best'}
NEGATIVE = {'bad', 'terrible', 'awful', 'hate', 'worst', 'disappointing', 'poor'}


def sentiment(text: str) -> float:
    words = [w.strip('.,!?').lower() for w in text.split()]
    score = sum(1 for w in words if w in POSITIVE) - sum(1 for w in words if w in NEGATIVE)
    return score


if __name__ == '__main__':
    examples = [
        'I am very happy with this product.',
        'This is the worst thing I have ever bought.',
        'Not bad, could be better.',
        'Absolutely fantastic experience.',
    ]

    for ex in examples:
        score = sentiment(ex)
        label = 'positive' if score > 0 else 'negative' if score < 0 else 'neutral'
        print(f'[{label}] score={score} -> {ex}')
