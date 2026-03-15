# sample2.py
# Train a simple sentiment classifier using TF-IDF and linear models (scikit-learn).

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


if __name__ == '__main__':
    texts = [
        'I love this product',
        'This is a great movie',
        'Terrible experience',
        'Worst service ever',
        'Highly recommend',
        'I hate it',
    ]
    labels = [1, 1, 0, 0, 1, 0]

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression(random_state=0)
    model.fit(X, labels)

    test_texts = ['Fantastic product', 'Not good at all']
    preds = model.predict(vectorizer.transform(test_texts))

    for text, pred in zip(test_texts, preds):
        print(f'"{text}" ->', 'positive' if pred == 1 else 'negative')
