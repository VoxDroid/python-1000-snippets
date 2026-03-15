# sample1.py
# Topic modeling using scikit-learn's Latent Dirichlet Allocation (LDA).

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def print_top_words(model, feature_names, n_top_words=5):
    for topic_idx, topic in enumerate(model.components_):
        top_features = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        print(f"Topic #{topic_idx}: {', '.join(top_features)}")


if __name__ == '__main__':
    documents = [
        'The cat sat on the mat',
        'Dogs and cats living together',
        'The economy is doing well',
        'Stock markets are up today',
        'My cat loves to chase mice',
        'Investors are optimistic about the economy',
    ]

    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents)

    lda = LatentDirichletAllocation(n_components=2, random_state=0, learning_method='batch')
    lda.fit(X)

    print('Top words per topic:')
    print_top_words(lda, vectorizer.get_feature_names_out(), n_top_words=5)
