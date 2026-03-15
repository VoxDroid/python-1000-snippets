# Neural Network

## Description
This snippet demonstrates a simple neural network (multi-layer perceptron) using `scikit-learn`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — train an MLP classifier and print accuracy.
- `sample2.py` — print predicted class probabilities for sample inputs.
- `sample3.py` — persist a trained model with joblib and reload it.

Run any of them with:

```bash
python python-1000-snippets/0253-Neural-Network/SAMPLES/sample1.py
```

## Output
Each sample prints classification accuracy, probabilities, or persistence validation.

## Explanation
- **Neural Network**: Uses a feedforward MLP to learn a classification boundary.
- **Logic**: Trains on synthetic data, then evaluates or serializes the model.
- **Use Case**: Useful for non-linear classification problems.
- **Best Practice**: Scale inputs; tune hidden layer sizes; handle convergence warnings by increasing iterations.
