# sample1.py
# Merge rows with evolving schema and print unified columns.


def unify_schema(rows):
    keys = set().union(*(r.keys() for r in rows))
    normalized = []
    for r in rows:
        normalized.append({k: r.get(k) for k in keys})
    return list(keys), normalized


if __name__ == '__main__':
    old = [{'col1': 1}, {'col1': 2}]
    new = [{'col1': 3, 'col2': 5}, {'col1': 4, 'col2': 6}]
    keys, merged = unify_schema(old + new)
    print('Schema evolved:', sorted(keys))
    print('Merged rows:', merged)
