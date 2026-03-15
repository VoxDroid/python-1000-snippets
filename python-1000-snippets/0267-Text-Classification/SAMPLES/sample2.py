# sample2.py
# Build a text classification pipeline with TF-IDF and Naive Bayes.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


if __name__ == '__main__':
    texts = [
        'good quality and fast shipping',
        'terrible customer service',
        'wonderful experience',
        'worst purchase ever',
        'highly recommend this',
        'do not buy this',
    ]
    labels = [1, 0, 1, 0, 1, 0]

    pipeline = (
        TfidfVectorizer(stop_words='english'),
        MultinomialNB(),
    )

    vectorizer = pipeline[0]
    classifier = pipeline[1]

    X = vectorizer.fit_transform(texts)
    classifier.fit(X, labels)

    test_texts = [
        'excellent product',
        'very poor quality',
        'I love it',
        'I hate this',
    ]
    preds = classifier.predict(vectorizer.transform(test_texts))
    print('Test texts:', test_texts)
    print('Predictions:', preds.tolist())
