# Named Entity Recognition

## Description
This snippet demonstrates Named Entity Recognition (NER) using `spacy`.

## Code
```python
# Note: Requires `spacy`. Install with `pip install spacy` and `python -m spacy download en_core_web_sm`
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    text = "Apple is based in California."
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("Entities:", entities)
except ImportError:
    print("Mock Output: Entities: [('Apple', 'ORG'), ('California', 'GPE')]")
```

## Output
```
Mock Output: Entities: [('Apple', 'ORG'), ('California', 'GPE')]
```
*(Real output with `spacy`: `Entities: [('Apple', 'ORG'), ('California', 'GPE')]`)*

## Explanation
- **Named Entity Recognition**: Identifies entities like organizations and locations.
- **Logic**: Processes text with `spacy` and extracts entities.
- **Complexity**: O(n) for n words.
- **Use Case**: Used for information extraction or knowledge graphs.
- **Best Practice**: Use pre-trained models; fine-tune for domains; handle ambiguities.