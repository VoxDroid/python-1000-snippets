# sample1.py
# Train a simple text classifier using TF-IDF and logistic regression.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


if __name__ == '__main__':
    texts = [
        'I love this product',
        'This is a great movie',
        'Terrible experience',
        'Worst service ever',
        'I would buy this again',
        'Not worth the money',
    ]
    labels = [1, 1, 0, 0, 1, 0]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression(random_state=0)
    model.fit(X, labels)

    acc = model.score(X, labels)
    print(f'Training accuracy: {acc:.2f}')

    # Predict on new texts
    new_texts = ['I really enjoyed this', 'I will never buy again']
    X_new = vectorizer.transform(new_texts)
    preds = model.predict(X_new)
    print('Predictions (1=positive, 0=negative):', preds.tolist())
