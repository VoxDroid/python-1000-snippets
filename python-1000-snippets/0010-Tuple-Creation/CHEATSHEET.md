# Tuple Creation Cheatsheet

## Creating tuples
```python
t = (1, 2, 3)
empty = ()
onelement = (42,)
```

## Unpacking
```python
x, y = (10, 20)
```

## Packing
```python
t = 1, 2, 3   # parentheses optional
```

## Immutability
- Tuples cannot be modified; reassignment creates a new tuple.
- Use for fixed collections, dictionary keys, or multiple return values.

## Useful tips
- Convert between lists and tuples: `list(t)`, `tuple(lst)`.
- Use tuples in loops: `for x, y in list_of_pairs:`

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

