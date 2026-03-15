# sample3.py
# Recognize named entities using a small custom dictionary of names and locations.

ENTITIES = {
    'PERSON': {'Alice', 'Bob', 'Charlie'},
    'LOCATION': {'Paris', 'New York', 'London'},
    'ORGANIZATION': {'OpenAI', 'Google', 'Microsoft'},
}


def extract_entities(text: str):
    words = [w.strip('.,!?') for w in text.split()]
    found = []
    for w in words:
        for label, vocabulary in ENTITIES.items():
            if w in vocabulary:
                found.append((label, w))
    return found


if __name__ == '__main__':
    text = 'Alice from OpenAI visited New York and then met Bob in London.'
    entities = extract_entities(text)
    print('Text:', text)
    print('Entities:', entities)
