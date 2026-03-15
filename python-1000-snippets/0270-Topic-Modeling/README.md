# Topic Modeling

## Description
This snippet demonstrates topic modeling using scikit-learn's Latent Dirichlet Allocation (LDA).

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — trains LDA and prints top words for each topic.
- `sample2.py` — assigns topic distributions to new documents after training.
- `sample3.py` — interprets topic-word distributions by showing the top words per topic.

Run a sample with:

```bash
python python-1000-snippets/0270-Topic-Modeling/SAMPLES/sample1.py
```

## Output
Each sample prints topic word lists or topic distributions for example text.

## Notes
- LDA is an unsupervised technique that models documents as mixtures of topics.
- Preprocessing text (removing stopwords, lemmatization) improves results.
- In real applications, use more data and tune the number of topics.
