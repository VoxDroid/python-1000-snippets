# sample2.py
# Apply schema evolution patch to existing data with default values.


def evolve_schema(rows, new_column, default=None):
    return [{**r, new_column: r.get(new_column, default)} for r in rows]


if __name__ == '__main__':
    rows = [{'col1': 1}, {'col1': 2}]
    evolved = evolve_schema(rows, 'col2', 0)
    print('Evolved rows:', evolved)
