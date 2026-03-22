# sample2.py
# Validate non-null and type constraints for data rows.


def row_validate(row):
    if row.get('id') is None:
        return False
    if not isinstance(row.get('value'), int):
        return False
    return 0 <= row['value'] <= 100


if __name__ == '__main__':
    rows = [{'id':1,'value':10},{'id':2,'value':-1},{'id':3,'value':50}]
    results = [row_validate(r) for r in rows]
    print('Row validation:', results)
