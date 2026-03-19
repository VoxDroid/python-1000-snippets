# sample2.py
# Save t-SNE embedding to a CSV file under /temp.

import os
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.manifold import TSNE


def main() -> None:
    os.makedirs("temp", exist_ok=True)

    data = load_iris(as_frame=True)
    X = data.data
    y = data.target

    tsne = TSNE(n_components=2, random_state=0, init="pca")
    embedding = tsne.fit_transform(X)

    df = pd.DataFrame(embedding, columns=["x", "y"])
    df["label"] = y
    out_path = "temp/tsne_iris.csv"
    df.to_csv(out_path, index=False)

    print("Saved embedding to", out_path)
    print(df.head())


if __name__ == "__main__":
    main()
