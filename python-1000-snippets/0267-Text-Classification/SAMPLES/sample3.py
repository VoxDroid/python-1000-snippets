# sample3.py
# Evaluate text classifier with train/test split and report accuracy.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    texts = [
        'I love this product',
        'This is a great movie',
        'Terrible experience',
        'Worst service ever',
        'I would buy this again',
        'Not worth the money',
        'Absolutely fantastic',
        'Very disappointing',
    ]
    labels = [1, 1, 0, 0, 1, 0, 1, 0]

    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=0)

    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(random_state=0)
    model.fit(X_train_vec, y_train)

    acc = model.score(X_test_vec, y_test)
    print(f'Test accuracy: {acc:.2f}')

    for text, pred in zip(X_test, model.predict(X_test_vec)):
        print(f'  {pred} <- {text}')
