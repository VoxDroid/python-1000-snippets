# sample1.py
# Simple rule-based sentiment scoring using keyword lists.

POSITIVE_WORDS = {'good', 'great', 'excellent', 'love', 'happy', 'fantastic', 'best', 'awesome'}
NEGATIVE_WORDS = {'bad', 'terrible', 'worst', 'hate', 'awful', 'disappointing', 'poor'}


def sentiment_score(text: str) -> float:
    tokens = text.lower().split()
    score = 0
    for t in tokens:
        if t.strip('.,!') in POSITIVE_WORDS:
            score += 1
        if t.strip('.,!') in NEGATIVE_WORDS:
            score -= 1
    return score


if __name__ == '__main__':
    samples = [
        'I love this product, it is excellent!',
        'This is the worst experience ever.',
        'It was okay, not great but not terrible.',
    ]

    for s in samples:
        score = sentiment_score(s)
        sentiment = 'positive' if score > 0 else 'negative' if score < 0 else 'neutral'
        print(f'Sentiment: {sentiment} (score={score}) -- "{s}"')
