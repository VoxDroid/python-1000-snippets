# sample1.py
# Extract simple named entities (dates, currencies, person names) using regex heuristics.

import re


def extract_entities(text):
    entities = []

    # Dates (MM/DD/YYYY or YYYY-MM-DD)
    for m in re.finditer(r"\b(\d{1,2}/\d{1,2}/\d{4})\b", text):
        entities.append(('DATE', m.group(1)))
    for m in re.finditer(r"\b(\d{4}-\d{2}-\d{2})\b", text):
        entities.append(('DATE', m.group(1)))

    # Currency amounts ($XX, €XX, etc.)
    for m in re.finditer(r"\b(\$\d+(?:\.\d{2})?)\b", text):
        entities.append(('MONEY', m.group(1)))

    # Simple proper nouns (capitalized words not at beginning of sentence)
    for m in re.finditer(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b", text):
        word = m.group(1)
        if word.lower() not in {'the', 'a', 'an'}:
            entities.append(('PROPER_NOUN', word))

    return entities


if __name__ == '__main__':
    text = 'Alice visited New York on 2025-07-04 and spent $120.50 on a taxi.'
    entities = extract_entities(text)
    print('Text:', text)
    print('Entities:', entities)
