# sample3.py
# Show how to interpret topic-word distributions from an LDA model.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def print_top_words(model, feature_names, n_top_words=5):
    for topic_idx, topic in enumerate(model.components_):
        top_features = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        print(f"Topic #{topic_idx}: {', '.join(top_features)}")


if __name__ == '__main__':
    docs = [
        'space exploration and rockets',
        'NASA launches a new satellite',
        'politics and elections in the country',
        'the government passed a new law',
        'space agencies are investing in exploration',
    ]

    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(docs)

    lda = LatentDirichletAllocation(n_components=2, random_state=0)
    lda.fit(X)

    print('Top words for each topic:')
    print_top_words(lda, vectorizer.get_feature_names_out(), n_top_words=5)
