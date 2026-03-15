# sample2.py
# Assign topics to new documents using a trained LDA model.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


if __name__ == '__main__':
    documents = [
        'A cat sits on a mat',
        'The stock market is up',
        'Investment and stocks',
        'Cats are great pets',
        'Economy and finance',
    ]

    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents)

    lda = LatentDirichletAllocation(n_components=2, random_state=0)
    lda.fit(X)

    new_docs = ['I love my cat', 'The market rallies today']
    new_X = vectorizer.transform(new_docs)
    topic_dist = lda.transform(new_X)

    for doc, dist in zip(new_docs, topic_dist):
        print(f'"{doc}" topic distribution: {dist.round(3).tolist()}')
